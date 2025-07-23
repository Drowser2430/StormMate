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
