import os
import re
import json
import time
import random
import requests
import schedule
from instagrapi import Client
import imageio
from moviepy.video.io.VideoFileClip import VideoFileClip

# ---------------------------------
# Configuration
# ---------------------------------
USERNAME = "your_instagram_username"   # <-- Replace with your Instagram username
PASSWORD = "your_instagram_password"   # <-- Replace with your Instagram password

DOWNLOAD_DIR = "downloaded_videos"
MIN_LIKES = 10000

# Number of followed users to check
FOLLOW_CHECK_LIMIT = 50
# Number of recent posts per user to inspect
MAX_MEDIA_PER_USER = 5

# Scheduled job interval in minutes
SCHEDULE_INTERVAL_MINUTES = 30

# JSON file to store reposted media PKs (to avoid duplicates)
REPOSTED_DB_FILE = "reposted_media.json"
# ---------------------------------

def ensure_download_dir():
    """Create the directory to store downloaded videos if it doesn't exist."""
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)


def load_reposted_db():
    """
    Load the set of reposted media PKs from a JSON file.
    Returns:
        set: A set of media PKs that have already been reposted.
    """
    if not os.path.isfile(REPOSTED_DB_FILE):
        return set()
    try:
        with open(REPOSTED_DB_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return set(data)
    except Exception as e:
        print(f"[ERROR] Could not load reposted DB: {e}")
        return set()


def save_reposted_db(reposted_pks):
    """
    Save the set of reposted media PKs to a JSON file.
    Parameters:
        reposted_pks (set): Set of media PKs.
    """
    try:
        with open(REPOSTED_DB_FILE, "w", encoding="utf-8") as f:
            json.dump(list(reposted_pks), f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[ERROR] Could not save reposted DB: {e}")


def login_to_instagram():
    """
    Log in using instagrapi.
    Returns:
        Client: An instance of instagrapi.Client if login is successful; else, None.
    """
    cl = Client()
    try:
        cl.login(USERNAME, PASSWORD)
        print(f"[INFO] Logged in as: {USERNAME}")
        return cl
    except Exception as e:
        print(f"[ERROR] Login failed: {e}")
        return None


def sanitize_caption_for_filename(caption, max_length=50):
    """
    Clean the caption so it can be safely used as part of a filename.
    Removes newlines, forbidden characters, and all '@' symbols.
    Parameters:
        caption (str): The original caption.
        max_length (int): Maximum length for the sanitized caption.
    Returns:
        str: A filename-safe version of the caption.
    """
    # Remove newlines
    safe_caption = re.sub(r'[\r\n]+', ' ', caption)
    # Remove forbidden characters
    safe_caption = re.sub(r'[<>:"/\\|?*]+', '', safe_caption)
    # Remove all '@' symbols
    safe_caption = safe_caption.replace('@', '')
    # Trim whitespace
    safe_caption = safe_caption.strip()
    # Truncate if too long
    if len(safe_caption) > max_length:
        safe_caption = safe_caption[:max_length] + "..."
    return safe_caption if safe_caption else "untitled"


def download_video(cl, media_pk):
    """
    Download a single-video post using its media PK.
    Parameters:
        cl (Client): An authenticated instagrapi.Client instance.
        media_pk (int): The primary key of the media to download.
    Returns:
        tuple: (local_path, caption_text) if successful, or (None, None) on error.
    """
    try:
        media_info = cl.media_info(media_pk)
    except Exception as e:
        print(f"[ERROR] Could not get media info for pk={media_pk}: {e}")
        return None, None

    if media_info.media_type != 2:
        print("[ERROR] Not a single video (media_type != 2).")
        return None, None

    video_url = media_info.video_url
    caption_text = media_info.caption_text or ""
    if not video_url:
        print("[ERROR] No video_url found.")
        return None, None

    safe_caption = sanitize_caption_for_filename(caption_text)
    filename = f"{safe_caption}_{media_pk}.mp4"
    local_path = os.path.join(DOWNLOAD_DIR, filename)

    print(f"[INFO] Downloading video from: {video_url}")
    try:
        response = requests.get(video_url, stream=True)
        response.raise_for_status()
    except Exception as e:
        print(f"[ERROR] Video download request failed: {e}")
        return None, None

    try:
        with open(local_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    except OSError as e:
        print(f"[ERROR] Cannot write file '{local_path}': {e}")
        return None, None

    print(f"[INFO] Saved video to: {local_path}")
    return local_path, caption_text


def reupload_video(cl, video_path, caption):
    """
    Re-upload the downloaded video with the same caption.
    Parameters:
        cl (Client): An authenticated instagrapi.Client instance.
        video_path (str): Path to the downloaded video file.
        caption (str): Caption to use for the re-upload.
    Returns:
        bool: True if the upload was successful; otherwise, False.
    """
    try:
        cl.video_upload(video_path, caption)
        print("[INFO] Video uploaded successfully.")
        return True
    except Exception as e:
        error_msg = str(e)
        if "moviepy" in error_msg.lower():
            print("[ERROR] Video upload failed: Ensure moviepy>=1.0.3 and ffmpeg installed & in PATH.")
        else:
            print(f"[ERROR] Video upload failed: {e}")
        return False


def find_one_video_over_10k_likes(cl, reposted_pks):
    """
    Scan the accounts you follow for the first single-video post with >10k likes
    that hasn't been reposted yet.
    Parameters:
        cl (Client): An authenticated instagrapi.Client instance.
        reposted_pks (set): Set of media PKs that have already been reposted.
    Returns:
        tuple or None: (media_pk, like_count, username) if found; otherwise, None.
    """
    try:
        my_user_id = cl.user_id
        following = cl.user_following(my_user_id, amount=FOLLOW_CHECK_LIMIT)
    except Exception as e:
        print(f"[ERROR] Could not fetch following list: {e}")
        return None

    for user in following.values():
        username = user.username
        print(f"[INFO] Checking @{username}...")
        try:
            medias = cl.user_medias_v1(user.pk, amount=MAX_MEDIA_PER_USER)
        except Exception as ex:
            print(f"[ERROR] Could not fetch posts for @{username}: {ex}")
            continue

        for media in medias:
            if media.media_type == 2:  # single video
                if media.pk not in reposted_pks:
                    like_count = media.like_count or 0
                    if like_count >= MIN_LIKES:
                        print(f"[INFO] Found video by @{username} with {like_count} likes.")
                        return (media.pk, like_count, username)
                    else:
                        print(f"[DEBUG] Video by @{username} has {like_count} likes (< {MIN_LIKES}).")
                else:
                    print(f"[DEBUG] Already reposted pk={media.pk}, skipping.")
            else:
                print(f"[DEBUG] Post by @{username} is not a single video.")
    return None


def scheduled_job(client, reposted_pks):
    """
    The job that finds a qualifying video and, if found, downloads and re-uploads it.
    Parameters:
        client (Client): The logged-in instagrapi.Client instance.
        reposted_pks (set): Set of already reposted media PKs.
    """
    print("[INFO] Searching for a qualifying single-video post with >10k likes...")
    result = find_one_video_over_10k_likes(client, reposted_pks)
    if result is None:
        print("[INFO] No suitable video found this run.")
        return
    media_pk, like_count, username = result
    print(f"[INFO] Processing video from @{username} with pk={media_pk} and {like_count} likes.")
    local_path, caption_text = download_video(client, media_pk)
    if not local_path:
        print("[ERROR] Video download failed. Skipping this video.")
        return
    if reupload_video(client, local_path, caption_text):
        reposted_pks.add(media_pk)
        save_reposted_db(reposted_pks)
        try:
            os.remove(local_path)
            print(f"[INFO] Removed local file: {local_path}")
        except Exception as e:
            print(f"[ERROR] Could not remove file '{local_path}': {e}")


def main():
    ensure_download_dir()
    reposted_pks = load_reposted_db()
    client = login_to_instagram()
    if not client:
        print("[ERROR] Exiting because login failed.")
        return

    while True:
        # Run the job once
        scheduled_job(client, reposted_pks)

        # Random delay between 30 and 120 minutes
        delay_minutes = random.randint(30, 120)

        # Compute exact next run time
        next_run_dt = datetime.datetime.now() + datetime.timedelta(minutes=delay_minutes)
        next_run_str = next_run_dt.strftime("%Y-%m-%d %H:%M:%S")

        print(f"[INFO] Next run in {delay_minutes} minute(s). Scheduled for: {next_run_str}")

        # Sleep for that many minutes (convert to seconds)
        time.sleep(delay_minutes * 60)


if __name__ == "__main__":
    main()

