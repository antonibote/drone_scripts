from dronekit import connect, VehicleMode
import time

# Connect to the Vehicle (replace with appropriate connection string)
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# Function to arm and take off
def arm_and_takeoff(target_altitude):
    while not vehicle.is_armable:
        print("Waiting for vehicle to be armable...")
        time.sleep(1)

    # Arm the vehicle
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for vehicle to arm...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(f"Altitude: {altitude}")
        if altitude >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Take off to 2 meters
arm_and_takeoff(2)

# Hover for 5 seconds
print("Hovering for 5 seconds...")
time.sleep(5)

# Land
print("Landing...")
vehicle.mode = VehicleMode("LAND")

# Close the vehicle object
vehicle.close()
