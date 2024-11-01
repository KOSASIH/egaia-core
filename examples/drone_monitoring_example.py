import time
from drone_control import Drone

# Example usage of drone monitoring
def drone_monitoring_example():
    # Create an instance of the drone
    drone = Drone()

    # Take off and start monitoring
    drone.takeoff()
    print("Drone is taking off...")

    # Monitor the drone's status and location
    while True:
        print(f"Drone status: {drone.status}, Location: {drone.location}")
        time.sleep(1)

if __name__ == "__main__":
    drone_monitoring_example()
