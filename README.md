# Qatar Airways Travel Alert Monitor

A small Python script that monitors the **Qatar Airways travel alerts page** and sends a **Telegram notification whenever a new alert is published**.

It uses the internal JSON API used by the website, so it avoids HTML scraping and is very reliable.

Alerts are checked automatically using GitHub Actions every few minutes.

---

## ✈️ What it does

- Fetches the latest travel alerts from Qatar Airways
- Detects new alerts
- Sends the full alert content to Telegram
- Prevents duplicate notifications
- Runs automatically via GitHub Actions

---

## 📡 Data Source

The script reads alerts from the public JSON endpoint used by the Qatar Airways website:

```
https://www.qatarairways.com/qr/qrweb/metabar-travel-alerts.en.json
```

---

## 🔔 Example Telegram Notification

```
🚨 Qatar Airways Travel Alert

08:00 GMT+3, 5 March 2026: Operational Update and Booking Assistance

Qatar Airways scheduled flight operations remain temporarily suspended due to the closure of Qatari airspace...
```

---

# ⚙️ Setup

## 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/qatar-alert-monitor.git
cd qatar-alert-monitor
```

---

## 2. Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

# 🤖 Create a Telegram Bot

1. Open Telegram and search for BotFather  
2. Run:

```
/newbot
```

3. Choose a bot name and username.

4. Save the Bot Token you receive.

---

# 💬 Get your Chat ID

1. Send a message to your bot in Telegram.

2. Open this URL in a browser:

```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
```

3. Find:

```
"chat": {
  "id": 123456789
}
```

That number is your CHAT_ID.

---

# 🔐 Configure GitHub Secrets

Go to:

Repository → Settings → Secrets and variables → Actions

Add the following:

| Secret | Value |
|------|------|
| BOT_TOKEN | your Telegram bot token |
| CHAT_ID | your Telegram chat ID |

---

# 🚀 GitHub Actions Automation

The repository includes a workflow that runs automatically.

```
.github/workflows/monitor.yml
```

It runs:

```
every 5 minutes
```

and executes:

```
python monitor.py
```

If a new alert appears, it sends a Telegram notification.

---

# 📂 Project Structure

```
qatar-alert-monitor
│
├ monitor.py
├ requirements.txt
├ seen_alerts.json
└ .github
    └ workflows
        └ monitor.yml
```

---

# 🧠 How It Works

1. Download alerts from the JSON API
2. Extract alert title and content
3. Compare with previously seen alerts
4. Send Telegram notification for new alerts
5. Save alerts to `seen_alerts.json`

---

# 🛠 Dependencies

- Python 3.10+
- requests

---

# ⚠️ Notes

- GitHub Actions schedules are **not guaranteed to run exactly every 5 minutes**
- The workflow may run with a small delay depending on GitHub load

---

# 📜 License

MIT License

---

# Disclaimer

This project is **not affiliated with or endorsed by Qatar Airways**.  
It simply monitors publicly available information for convenience.