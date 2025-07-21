# stormmate_simulation.py

class SimulatedUPS:
    def __init__(self):
        self.status = "on_grid"
        self.battery_level = 100

    def get_status(self):
        return self.status

    def simulate_outage(self):
        self.status = "on_battery"

    def get_battery_level(self):
        return self.battery_level


class SimulatedSmartPlug:
    def __init__(self, name):
        self.name = name
        self.powered = True

    def detect_power(self, ups_status):
        self.powered = (ups_status == "on_grid")

    def get_status(self):
        return f"{self.name} is {'ON' if self.powered else 'OFF'}"


class SimulatedLight:
    def __init__(self, location):
        self.location = location
        self.brightness = 0

    def turn_on(self):
        self.brightness = 100
        print(f"🟡 {self.location} light turned ON at brightness {self.brightness}%.")

    def turn_off(self):
        self.brightness = 0
        print(f"⚫ {self.location} light turned OFF.")


def simulate_stormmate():
    ups = SimulatedUPS()
    router_plug = SimulatedSmartPlug("Router")
    light = SimulatedLight("Living Room")

    print("🌤️ System running normally...")
    print(router_plug.get_status())

    # Simulate outage
    ups.simulate_outage()
    router_plug.detect_power(ups.get_status())

    print("\n⚠️ Power outage detected!")
    print(router_plug.get_status())
    print("🔊 Alexa: Power outage detected. Activate StormMate?")
    print("🗣️ User: Yes.")
    print("🔊 Alexa: Activating StormMate...")

    # Trigger lights
    light.turn_on()

    # Simulate SMS alert (print only)
    print("📩 Sending SMS alert: 'Power outage at home. StormMate activated.'")


if __name__ == "__main__":
    simulate_stormmate()
