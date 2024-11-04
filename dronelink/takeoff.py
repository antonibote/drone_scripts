from dronLink.Dron import Dron
import time

# Initialize the drone
dron = Dron()

print("Activating")

dron.connect('udp:127.0.0.1:14551', 115200)

dron.arm()
print("Armed")

dron.takeOff(2)

time.sleep(5)

dron.RTL()

print("Mission complete!")
