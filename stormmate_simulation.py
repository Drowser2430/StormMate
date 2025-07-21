# stormmate_simulation.py

class SimulatedUPS:
    def __init__(self):
        self.status = "on_grid"

    def get_status(self):
        return self.status

    def simulate_outage(self):
        self.status = "on_battery"

class SimulatedSmartPlug:
    def __init__(self):
        self.powered = True

    def turn_off(self):
        self.powered = False
        print("🔌 Smart Plug turned OFF")

    def turn_on(self):
        self.powered = True
        print("🔌 Smart Plug turned ON")

class SimulatedLight:
    def turn_on(self):
        print("💡 Light ON")

    def turn_off(self):
        print("💡 Light OFF")

def alexa_prompt():
    print("Alexa: Power outage detected. Activate StormMate?")
    user_response = input("User response (yes/no): ").strip().lower()
    return user_response == "yes"

def run_simulation():
    ups = SimulatedUPS()
    plug = SimulatedSmartPlug()
    light = SimulatedLight()

    print("⚠️ Simulating power outage...")
    ups.simulate_outage()

    if ups.get_status() == "on_battery":
        if alexa_prompt():
            plug.turn_on()
            light.turn_on()
            print("📨 SMS Alert: Power outage detected. StormMate activated.")
        else:
            print("Alexa: Okay, StormMate not activated.")

# Run the simulation
if __name__ == "__main__":
    run_simulation()
