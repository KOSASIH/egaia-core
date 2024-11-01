import random
import time

class SensorIntegration:
    """Class for integrating sensors for data collection."""
    
    def __init__(self):
        self.gps_data = None
        self.imu_data = None
        self.camera_data = None

    def read_gps(self):
        """Simulate reading GPS data."""
        self.gps_data = {
            'latitude': random.uniform(-90, 90),
            'longitude': random.uniform(-180, 180),
            'altitude': random.uniform(0, 1000)
        }
        print(f"GPS Data: {self.gps_data}")

    def read_imu(self):
        """Simulate reading IMU data."""
        self.imu_data = {
            'acceleration': [random.uniform(-10, 10) for _ in range(3)],
            'gyroscope': [random.uniform(-180, 180) for _ in range(3)],
            'orientation': [random.uniform(0, 360) for _ in range(3)]
        }
        print(f"IMU Data: {self.imu_data}")

    def capture_image(self):
        """Simulate capturing an image from the camera."""
        self.camera_data = f"Image_{int(time.time())}.jpg"
        print(f"Captured Image: {self.camera_data}")

    def collect_data(self):
        """Collect data from all sensors."""
        self.read_gps()
        self.read_imu()
        self.capture_image()

# Example usage
if __name__ == "__main__":
    sensor_integration = SensorIntegration()
    while True:
        sensor_integration.collect_data()
        time.sleep(5)  # Collect data every 5 seconds
