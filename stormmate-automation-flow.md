# ⚡ StormMate: Smart Emergency Lighting Automation Flow

> A plug-and-play automation system to keep your lights and Wi-Fi running during climate-related blackouts.

---

## 🔁 Automation Flow Overview

This flow outlines how StormMate works when an outage occurs and how it restores normal function after.

```
[ Power Drop Detected ]
           ↓
[ Smart Plug Triggers Backup Power Source ]
           ↓
[ Lights + Wi-Fi Router Switched to Battery Power ]
           ↓
[ Twilio Webhook Sends SMS Alert to Emergency Contact ]
           ↓
[ Optional: Alexa/Google Routine Activates "Storm Mode" ]
           ↓
[ Normal Power Restored ]
           ↓
[ Devices Revert to Primary Power Source ]
           ↓
[ User Notified of Power Recovery ]
```

---

## 🧩 System Components

- **Smart Plug** (TP-Link, Kasa, or similar)
- **Uninterruptible Power Supply (UPS)** for router + light
- **LED Lightbulb** (energy-efficient, emergency compatible)
- **Wi-Fi Router**
- **Twilio API** for SMS notifications
- **Optional Voice Assistant** (Alexa / Google Home)

---

## 💡 Sample Routine Trigger (Alexa / Google Home)

> “Alexa, activate Storm Mode.”

- Turn on hallway/stairwell light (plugged into smart plug)
- Lower brightness to conserve power
- Send verbal confirmation: “Storm Mode activated. Devices running on backup power.”
- Optionally trigger routine to check weather via assistant

---

## 📱 SMS Alert Logic (Twilio Webhook)

- If Wi-Fi signal or smart plug voltage drops
- Trigger webhook → send SMS:

  ```
  Power outage detected at [address or label].
  Devices switched to backup power.
  This message was sent by your StormMate system.
  ```

---

## ✅ Status Monitoring (Optional)

Integrate with a smart home hub or dashboard to monitor:

- Power status (grid vs backup)
- Battery level
- Connectivity status
- Historical outage logs

---

## 🛠️ Future Upgrades (Not Yet Implemented)

- Solar UPS system
- AI anomaly detection for outage prediction
- Voice-controlled reset commands
- API integration with insurance claims platforms

---

Need support or commercial licensing?  
📩 Contact: [dariusrowserbiz@gmail.com](mailto:dariusrowserbiz@gmail.com)