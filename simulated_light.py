class SimulatedLight:
    def __init__(self, name):
        self.name = name
        self.state = "off"
        self.brightness = 0

    def turn_on(self):
        self.state = "on"
        print(f"{self.name} light turned ON.")

    def turn_off(self):
        self.state = "off"
        print(f"{self.name} light turned OFF.")

    def set_brightness(self, level):
        self.brightness = level
        print(f"{self.name} light brightness set to {level}.")
