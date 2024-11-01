import time
import random

class DataTransmission:
    """Class for transmitting data to cloud storage."""
    
    def __init__(self):
        self.data_buffer = []

    def send_data(self, data):
        """Simulate sending data over a network."""
        self.data_buffer.append(data)
        print(f"Sending data: {data}")
        time.sleep(random.uniform(0.5, 2))  # Simulate network latency
        print("Data sent successfully.")

    def transmit_to_cloud(self, data_buffer):
        """Transmit the data buffer to cloud storage."""
        for data in data_buffer:
            self.send_data(data)
        self.data_buffer = []

# Example usage
if __name__ == "__main__":
    data_transmission = DataTransmission()
    sensor_integration = SensorIntegration()

    while True:
        sensor_integration.collect_data()
        data_transmission.transmit_to_cloud([sensor_integration.gps_data, sensor_integration.imu_data, sensor_integration.camera_data])
        time.sleep(10)  # Transmit data every 10 seconds
