# === Simulated Hardware Classes ===

class SimulatedUPS:
    def __init__(self):
        self.status = "on_grid"
        self.battery_level = 100

    def get_status(self):
        return self.status

    def get_battery_level(self):
        return self.battery_level

    def simulate_outage(self):
        self.status = "on_battery"
        self.battery_level -= 10

    def restore_power(self):
        self.status = "on_grid"
        self.battery_level = 100


class SimulatedSmartPlug:
    def __init__(self):
        self.power_status = "on"

    def detect_power(self, ups_status):
        return "off" if ups_status == "on_battery" else "on"


class SimulatedLight:
    def __init__(self, name):
        self.name = name
        self.status = "off"
        self.brightness = 0

    def turn_on(self, brightness=100):
        self.status = "on"
        self.brightness = brightness
        print(f"{self.name} turned on at {brightness}% brightness")

    def turn_off(self):
        self.status = "off"
        self.brightness = 0
        print(f"{self.name} turned off")


# === Core Simulation Logic ===

def simulate_alexa_prompt():
    print("Alexa: Darius, power outage detected. Activate StormMate?")
    response = input("User: ").lower()
    return response in ["yes", "y"]


def automation_flow(lights):
    print("Alexa: Okay, activating StormMate. Lighting your living room.")
    for light in lights:
        light.turn_on(70)
    print("Sending SMS alert to emergency contacts... (simulated)")


# === AI Logic Section ===

def get_user_preference(current_hour):
    if 6 <= current_hour < 9:
        return ["kitchen"]
    elif 18 <= current_hour < 22:
        return ["living_room", "hallway"]
    else:
        return ["bedroom"]

def detect_anomaly(ups_status_history):
    if len(ups_status_history) < 3:
        return False
    return ups_status_history[-1] != ups_status_history[-2] and ups_status_history[-2] != ups_status_history[-3]

    # === Main Simulation Execution ===

if __name__ == "__main__":
    ups = SimulatedUPS()
    smart_plug = SimulatedSmartPlug()
    lights = {
        "kitchen": SimulatedLight("Kitchen Light"),
        "living_room": SimulatedLight("Living Room Light"),
        "hallway": SimulatedLight("Hallway Light"),
        "bedroom": SimulatedLight("Bedroom Light"),
    }

    ups_status_history = []

    print("Simulating power outage...")
    ups.simulate_outage()
    ups_status = ups.get_status()
    ups_status_history.append(ups_status)

    if ups_status == "on_battery":
        if simulate_alexa_prompt():
            import datetime
            current_hour = datetime.datetime.now().hour
            preferred_rooms = get_user_preference(current_hour)
            automation_flow([lights[room] for room in preferred_rooms])
            if detect_anomaly(ups_status_history):
                print("⚠️ Anomaly detected in UPS status pattern.")

# Simulated UPS
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


# Simulated Smart Plug
class SimulatedSmartPlug:
    def __init__(self):
        self.power_on = True

    def detect_power(self):
        return self.power_on

    def simulate_power_loss(self):
        self.power_on = False


# Simulated Light
class SimulatedLight:
    def __init__(self, name):
        self.name = name
        self.state = "off"
        self.brightness = 0

    def turn_on(self, brightness=100):
        self.state = "on"
        self.brightness = brightness
        print(f"{self.name} light ON at {brightness}% brightness.")

    def turn_off(self):
        self.state = "off"
        self.brightness = 0
        print(f"{self.name} light OFF.")

