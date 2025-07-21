
# stormmate twilio webhook setup

This guide walks you through integrating Twilio with your StormMate system to send SMS alerts when a power outage is detected.

---

## 🔧 prerequisites

- A [Twilio](https://www.twilio.com/) account
- A verified phone number in Twilio
- A webhook URL (hosted on a cloud function or your own server)
- Node.js or Python (for webhook scripting)

---

## 🚨 goal

When the smart plug detects power loss, the webhook triggers Twilio to send an SMS alert to a saved contact (e.g., a loved one or emergency number).

---

## 🛠️ setup steps

### 1. get your twilio credentials

Log into [Twilio Console](https://www.twilio.com/console) and grab:
- `ACCOUNT_SID`
- `AUTH_TOKEN`
- Your Twilio phone number

---

### 2. sample webhook in python (flask)

```python
from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)

@app.route("/stormmate-alert", methods=["POST"])
def send_sms():
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="🚨 StormMate Alert: Power outage detected.",
        from_="+1234567890",  # Your Twilio number
        to="+1987654321"      # Recipient's number
    )

    return {"status": "sent"}, 200

if __name__ == "__main__":
    app.run()
```

---

### 3. host webhook

- Deploy to [Render](https://render.com/), [Railway](https://railway.app/), or your own server
- Set the URL in your smart plug logic (e.g., `https://yourdomain.com/stormmate-alert`)

---

### 4. test

Simulate power loss and verify SMS is received. You can test via `curl`:

```bash
curl -X POST https://yourdomain.com/stormmate-alert
```

---

## 📩 next steps

- Add fallback contact options
- Log alert timestamps to a simple sheet or database
- Consider adding voice alerts or push notifications

