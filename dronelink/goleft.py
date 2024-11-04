from dronLink.Dron import Dron
import time

# Initialize the drone
dron = Dron()

print("Activating")

dron.connect('udp:127.0.0.1:14551', 115200)

dron.arm()

dron.takeOff(5)

dron.goto(0, -3, 0)

time.sleep(5)

dron.RTL()

print("Mission complete!")
