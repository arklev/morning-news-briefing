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
   Edit the `.env` file with your keys (already pre-configured in this setup).

## Running

### Manual Test
```bash
~/morning_briefing/venv/bin/python3 ~/morning_briefing/main.py
```

### Automatic Daily Execution (Cron)
To run every morning at 8:00 AM, add this to your crontab (`crontab -e`):
```bash
0 8 * * * /home/arklev/morning_briefing/venv/bin/python3 /home/arklev/morning_briefing/main.py
```

## Features
- **RSS Fetching:** Pulls from TechCrunch, The Verge, and AI News.
- **AI Summary:** Uses Google Gemini 1.5 Flash (low latency/high efficiency).
- **Lightweight:** Minimal dependencies, low memory footprint.
- **Error Handling:** Logs failures to `morning_briefing.log`.
- **ntfy Integration:** Sends formatted notifications to your phone.

## Troubleshooting
Check `morning_briefing.log` for errors if notifications are not arriving.
