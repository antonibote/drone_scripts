from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# Connect to the Vehicle
vehicle = connect('127.0.0.1:14550', wait_ready=True)

def arm_and_takeoff(target_altitude):
    while not vehicle.is_armable:
        print("Waiting for vehicle to be armable...")
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for vehicle to arm...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(target_altitude)

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        if altitude >= target_altitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Function to move to a specific location
def move_to_location(lat_offset, lon_offset):
    current_location = vehicle.location.global_relative_frame
    target_location = LocationGlobalRelative(current_location.lat + lat_offset, current_location.lon + lon_offset, current_location.alt)
    vehicle.simple_goto(target_location)

# Take off to 5 meters
arm_and_takeoff(5)

# First movement: 3 meters to the left
print("Moving 3 meters to the left...")
move_to_location(0, -0.00003)
time.sleep(2)  # Pause for 2 seconds

# Second movement: 3 more meters to the left
print("Moving another 3 meters to the left...")
move_to_location(0, -0.00003)
time.sleep(2)  # Pause for 2 seconds

# Third movement: another 3 meters to the left
print("Moving another 3 meters to the left...")
move_to_location(0, -0.00003)
time.sleep(2)  # Pause for 2 seconds

# Land
print("Landing...")
vehicle.mode = VehicleMode("LAND")

# Close the vehicle object
vehicle.close()
