import unittest

class TestDroneControl(unittest.TestCase):
    """Unit tests for drone control systems."""

    def test_takeoff(self):
        # Example test for drone takeoff
        drone = Drone()
        drone.takeoff()
        self.assertTrue(drone.is_flying)

    def test_land(self):
        # Example test for drone landing
        drone = Drone()
        drone.takeoff()
        drone.land()
        self.assertFalse(drone.is_flying)

if __name__ == "__main__":
    unittest.main()
