# Morning News Briefing

A lightweight automated news briefing system designed for Debian on older hardware.

## Installation (Debian)

1. **Install Python 3 and venv:**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```

2. **Setup the project:**
   ```bash
   cd ~/morning_briefing
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   Edit the .env file with your keys. Required variables:
   - GEMINI_API_KEY: Your Google Gemini API key.
   - NOTIFICATION_CHANNEL: 'discord' or 'ntfy'.
   - DISCORD_WEBHOOK_URL: (If using Discord) Your webhook URL.
   - NTFY_URL, NTFY_USER, NTFY_PASS: (If using ntfy) Your ntfy.sh settings.

## Running

### Manual Test
```bash
~/morning_briefing/venv/bin/python3 ~/morning_briefing/main.py
```

### Automatic Daily Execution (Cron)
To run every morning at 8:00 AM, add this to your crontab (crontab -e):
```bash
0 8 * * * /home/arklev/morning_briefing/venv/bin/python3 /home/arklev/morning_briefing/main.py
```

## Features
- **RSS Fetching:** Targeted Tech news from Ynet RSS feeds.
- **AI Summary:** Uses Google Gemini for high-quality, concise briefings.
- **Hebrew Support:** Delivers news summaries in Hebrew.
- **Multi-Channel Notifications:** Support for Discord (with rich Embeds) and ntfy.
- **Lightweight:** Minimal dependencies, low memory footprint.
- **Robust Logging:** Detailed execution logs saved locally.

## Troubleshooting
Check morning_briefing.log for errors if notifications are not arriving.
