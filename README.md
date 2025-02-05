# 🚀 Instagram Video Reposter Bot 📱

## 🔥 Overview

This script automates the process of reposting Instagram videos with more than **10,000 likes**! 🎥 It finds videos from accounts you follow, downloads them, and re-uploads them to your account. You can schedule this to run every **30 minutes** 🔄. It's perfect for boosting engagement and growing your profile! 📈

## 🛠 Features

- **Automatic Reposting**: Finds videos with 10k+ likes and reposts them to your account 🔁.
- **Avoid Duplicates**: Keeps track of reposted media to avoid reposting the same video 🛑.
- **Scheduled Posts**: Runs automatically at a set interval (default: **30 minutes**) 🕒.
- **Video Download and Upload**: Downloads videos and re-uploads them with the same caption ✨.
- **Optimized for Engagement**: Focuses on high-likes content to increase visibility 🚀.

## 📦 Requirements

To run this script, you'll need to install the following Python libraries:

- [instagrapi](https://pypi.org/project/instagrapi/) 🧩
- [requests](https://pypi.org/project/requests/) 📦
- [moviepy](https://pypi.org/project/moviepy/) 🎬
- [schedule](https://pypi.org/project/schedule/) ⏰
- [imageio](https://pypi.org/project/imageio/) 🖼

You can install them via `pip`:

```bash
pip install instagrapi requests moviepy schedule imageio
```

## ⚙️ Setup

1. Clone this repository or download the script file.
2. Replace the placeholder values in the **Configuration** section with your Instagram account details and preferred settings:
   - **USERNAME**: Your Instagram username 🔑
   - **PASSWORD**: Your Instagram password 🔒
   - **DOWNLOAD_DIR**: Directory where videos will be saved 💾
   - **MIN_LIKES**: Minimum likes to consider reposting (default: **10,000** 👍)
   - **SCHEDULE_INTERVAL_MINUTES**: Time interval for the scheduled job (default: **30 minutes** ⏳)

## 🏃‍♂️ How to Run

Once you've set up the configuration, simply run the script:

```bash
python instagram_video_reposter.py
```

The script will:

- Log in to Instagram 📱
- Check the accounts you follow for videos with 10k+ likes 🔍
- Download and re-upload qualifying videos 📥 ➡️ 📤
- Run the job every **30 minutes** by default ⏰

You can customize the job interval by changing the **SCHEDULE_INTERVAL_MINUTES** in the code 🛠.

## 💾 Data Management

The script uses a JSON file (`reposted_media.json`) to store the media primary keys (PKs) of videos that have already been reposted. This ensures that no video is reposted more than once 🔄.

## 📈 Why Use This?

- **Increase Visibility**: Reposting viral content helps boost your profile's engagement 📊.
- **Save Time**: Automate the process of finding, downloading, and reposting videos ⏳.
- **Easy to Use**: Once set up, the bot works on autopilot, so you can focus on other tasks 🔧.

## 🚨 Important Notes

- **Disclaimer**: Botting is against Instagram's Terms of Service, and misuse can lead to account suspension or bans. Use this tool responsibly and at your own risk. ⚠️
- Be mindful of Instagram's terms of service regarding automated actions ⚖️.
- Ensure your account is secure and use this tool responsibly for **ethical content curation** 💡.

## 📢 Contact

For any issues or questions, feel free to contact me on [Instagram](https://www.instagram.com/ambryhoprojekt/) 📲.

---

Happy Reposting! ✨
