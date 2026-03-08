import requests
import html
import re
import json
import os

URL = "https://www.qatarairways.com/qr/qrweb/metabar-travel-alerts.en.json"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

STATE_FILE = "seen_alerts.json"


def clean_html(text):
    text = html.unescape(text)
    text = re.sub("<.*?>", "", text)
    return text.strip()


def get_alerts():
    r = requests.get(URL)
    r.raise_for_status()

    data = r.json()

    alerts = []

    for item in data["alerts"]:
        for title in item["titles"]:
            alerts.append({
                "title": title["alertTitles"],
                "content": clean_html(title["description"])
            })

    return alerts


def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": message
    })


def load_seen():
    if not os.path.exists(STATE_FILE):
        return []

    with open(STATE_FILE) as f:
        return json.load(f)


def save_seen(data):
    with open(STATE_FILE, "w") as f:
        json.dump(data, f)


def main():

    alerts = get_alerts()
    seen = load_seen()

    for alert in alerts:

        key = alert["title"]

        if key not in seen:

            message = f"""
🚨 Qatar Airways Travel Alert

{alert['title']}

{alert['content']}
"""

            send_telegram(message)

            seen.append(key)

    save_seen(seen)


if __name__ == "__main__":
    main()