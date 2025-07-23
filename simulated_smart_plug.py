class SimulatedSmartPlug:
    def __init__(self):
        self.power = True

    def detect_power_status(self):
        return "on" if self.power else "off"

    def simulate_cut_power(self):
        self.power = False

    def restore_power(self):
        self.power = True
