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

# Take off to 2 meters
arm_and_takeoff(2)

# Hover for 5 seconds
print("Hovering for 5 seconds...")
time.sleep(5)

# Move 3 meters to the left
print("Moving 3 meters to the left...")
current_location = vehicle.location.global_relative_frame
target_location = LocationGlobalRelative(current_location.lat, current_location.lon - 0.00003, current_location.alt)
vehicle.simple_goto(target_location)

# Hover for 5 seconds
time.sleep(5)

# Land
print("Landing...")
vehicle.mode = VehicleMode("LAND")

# Close the vehicle object
vehicle.close()
