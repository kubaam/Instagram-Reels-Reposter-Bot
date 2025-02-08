# 🚀 Instagram Video Reposter Bot 📱

## 🔥 Overview

This script automates the process of reposting Instagram videos with more than **10,000 likes**! 🎥 It finds videos from accounts you follow, downloads them, and re-uploads them to your account. You can schedule this to run every **30 minutes** 🔄. It's perfect for boosting engagement and growing your profile! 📈

## 🛠 Features

- **Automatic Reposting**: Finds videos with 10k+ likes and reposts them to your account 🔁.
- **Avoid Duplicates**: Keeps track of reposted media to avoid reposting the same video 🛑.
- **Scheduled Posts**: Runs automatically at random interval (between: **30 and 120 minutes**) 🕒.
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
python main.py
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

<!--
- Instagram Video Reposter
- Instagram Video Reposting Bot
- Best Instagram Repost Bot
- Automated Instagram Video Reposter
- Instagram Content Reposter Tool
- Instagram Reposting Automation
- Instagram Video Post Scheduler
- Instagram Video Auto Reposter
- Instagram Video Reshare Bot
- Instagram Video Reposter Free Download
- Instagram Post Reposter Bot
- Instagram Video Reshare Automation
- Instagram Reposter for Marketing
- Instagram Video Content Automation
- Instagram Repost Bot Features
- Instagram Auto Video Reposting Tool
- Instagram Video Reposter 2024
- Instagram Video Reposting Software
- Instagram Post Scheduler for Videos
- Free Instagram Video Reposter Tool
- Instagram Video Repost Bot for Business
- Instagram Auto Reshare Software
- Instagram Video Reposting Service
- Instagram Marketing Automation Tools
- Instagram Video Repost Bot Setup
- How to Repost Videos on Instagram Automatically
- Instagram Video Reposting Strategy
- Instagram Repost Tool for Growth
- Best Instagram Video Repost Bot 2024
- Instagram Automation for Video Posts
- Instagram Content Repost Scheduling Tool
- Instagram Post Reposting Bot for Influencers
- Instagram Video Repost Scheduler 2024
- Instagram Video Reposting Solution
- Instagram Video Auto Reposting Tips
- Instagram Video Reshare Automation Guide
- Best Instagram Video Post Reposting Tools
- Instagram Video Reposting Tutorial
- Instagram Video Reposting Features Explained
- Instagram Auto Video Reshare Tool
- Instagram Video Marketing Automation
- Instagram Reposting Service for Influencers
- Instagram Video Post Reposting Bot
- Instagram Reshare Tool for Entrepreneurs
- Instagram Video Reposter Customization
- Instagram Video Reposter for Content Creators
- Instagram Marketing Bot for Video Posts
- How to Automate Instagram Video Sharing
- Instagram Video Reposting Bot for Pages
- Instagram Video Reposting Bot for 2024
- Instagram Video Post Automation Tools
- Instagram Video Content Reposting Tips
- Instagram Repost Bot for Business Growth
- Instagram Auto Reshare Bot Guide
- Instagram Video Reposting System
- How to Repost Instagram Videos Automatically
- Instagram Automation for Video Resharing
- Instagram Video Repost Tool for Marketing
- Instagram Video Repost Bot for Social Media Managers
- Instagram Automated Video Reshare Features
- Instagram Post Scheduler for Video Marketing
- Instagram Reposting Software for Business
- Instagram Reposting Automation for Marketing
- Instagram Video Reposting Tools for Influencers
- Instagram Content Reposting Strategy
- Instagram Post Reposting Automation 2024
- Instagram Video Reposting Bot for Instagram Stories
- Instagram Video Repost API
- Instagram Video Post Automation Platform
- Instagram Video Reposting for Growth
- Instagram Automated Video Resharing Bot
- Instagram Video Reposting API Integration
- Instagram Video Content Reposting Automation
- Instagram Video Reposting Best Practices
- Instagram Video Reshare Bots for Influencers
- Instagram Video Auto-Reshare System
- Instagram Video Reposting Automation Software
- Instagram Automated Video Reposting 2024
- Instagram Reposting Bot for Engagement
- Instagram Video Post Reposting Guide
- Instagram Video Reposter API Support
- Instagram Content Automation Bot
- Instagram Video Repost Bot for Pages
- Instagram Video Repost Software 2024
- Instagram Post Automation for Video Sharing
- Instagram Video Reposting Solutions for Marketing
- Instagram Video Reposter with Analytics
- Instagram Video Reshare Bot Features
- Instagram Repost Bot for Content Strategy
- Instagram Video Reposting Service for Growth
- Instagram Reposting for Video Posts 2024
- Instagram Automated Video Post Sharing
- Instagram Repost Tool for Video Sharing
- Instagram Video Reposting App for Marketers
- Instagram Video Reposting with Multi-Account Support
- Instagram Video Reposting Tool for Pages
- Instagram Marketing Automation Bot for Videos
-->


Happy Reposting! ✨
