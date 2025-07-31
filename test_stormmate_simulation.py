import unittest
from stormmate_simulation import (
    SimulatedUPS,
    SimulatedSmartPlug,
    SimulatedLight,
    get_user_preference,
    detect_anomaly,
)

class TestStormMateSimulation(unittest.TestCase):

    def test_ups_simulate_outage(self):
        ups = SimulatedUPS()
        ups.simulate_outage()
        self.assertEqual(ups.get_status(), "on_battery")
        self.assertLess(ups.get_battery_level(), 100)

    def test_ups_restore_power(self):
        ups = SimulatedUPS()
        ups.simulate_outage()
        ups.restore_power()
        self.assertEqual(ups.get_status(), "on_grid")
        self.assertEqual(ups.get_battery_level(), 100)

    def test_smart_plug_detection(self):
        plug = SimulatedSmartPlug()
        self.assertEqual(plug.detect_power("on_grid"), "on")
        self.assertEqual(plug.detect_power("on_battery"), "off")

    def test_light_behavior(self):
        light = SimulatedLight("Test Light")
        light.turn_on(80)
        self.assertEqual(light.status, "on")
        self.assertEqual(light.brightness, 80)
        light.turn_off()
        self.assertEqual(light.status, "off")
        self.assertEqual(light.brightness, 0)

    def test_get_user_preference(self):
        self.assertEqual(get_user_preference(7), ["kitchen"])
        self.assertEqual(get_user_preference(19), ["living_room", "hallway"])
        self.assertEqual(get_user_preference(23), ["bedroom"])

    def test_detect_anomaly(self):
        history_normal = ["on_grid", "on_grid", "on_grid"]
        history_anomalous = ["on_grid", "on_battery", "on_grid"]
        self.assertFalse(detect_anomaly(history_normal))
        self.assertTrue(detect_anomaly(history_anomalous))

if __name__ == "__main__":
    unittest.main()
