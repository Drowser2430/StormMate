
# 🧠 StormMate System Diagram

This file outlines the system components and flow of StormMate — a smart emergency lighting + Wi-Fi backup system powered by automation and SMS alerts.

---

## ⚡ System Flow

1. **Power Detected**
    - System continuously monitors the power supply.
2. **Power Loss Detected**
    - UPS (Uninterruptible Power Supply) activates.
    - Smart plugs automatically switch to critical devices:
        - LED lights
        - Wi-Fi router
    - Twilio webhook sends SMS alert to:
        - Emergency contact(s)
        - Optional: insurance provider or neighbor
3. **Storm Mode Engaged**
    - Smart speaker announces: “Emergency mode activated. Lighting and Wi-Fi systems running on backup.”
    - Secondary routines can dim lights to conserve power or flash lights for attention if evacuation is needed.
4. **Power Restoration**
    - System resumes normal mode.
    - SMS update sent confirming power return.

---

## 🔧 Components

| Component           | Role                                                                 |
|---------------------|----------------------------------------------------------------------|
| Smart Plug          | Controls power delivery to connected devices                         |
| UPS                 | Keeps key devices (router, lights) powered during outages            |
| LED Lightbulbs      | Energy-efficient lighting solution                                   |
| Wi-Fi Router        | Maintains internet connection via backup power                       |
| Twilio Webhook      | Sends SMS alerts during events                                       |
| Alexa/Google Routines| Engages "Storm Mode" announcements and smart actions                |

---

## 📍 Example Use Case

> “During Hurricane Zeta, our home lost power for 36 hours. StormMate kept our router and hallway light running the entire time. We received an SMS update when the outage occurred — and again when it was restored. Life-saving peace of mind.”

---

## 🛠️ Diagram Notes

See included image file `stormmate_system_diagram.png` for a simplified visual.
