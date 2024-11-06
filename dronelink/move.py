from dronLink.Dron import Dron
import time

dron = Dron()

print("Activating")

dron.connect('udp:127.0.0.1:14551', 115200)

dron.arm()
print("Armed") 

print("Taking off")
dron.takeOff(5)

dron.fixHeading()
print("Heading fixed")

dron.setMoveSpeed(1)
print(f"Speed set to {1} m/s")

print("Moving 3 meters to the left") 
dron.move_distance("Left", 3)

time.sleep(5)

print("Returning to base")
dron.RTL()

print("Mission complete!")
