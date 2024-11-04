from dronLink.Dron import Dron
from dronLink.Camera import Camera
import time
import cv2

print("Initializing drone and camera.")
dron = Dron()
camera = Camera()

print("Connecting to the drone.")
dron.connect('udp:127.0.0.1:14551', 115200)

print("Arming the drone.")
dron.arm()
print("Taking off to 5 meters.")
dron.takeOff(5)

for i in range(3):
    print(f"Moving left {i + 1}/3, 3 meters.")
    dron.move_distance("Left", 3)

    time.sleep(3)
    print("Taking a picture.")
    ret, frame = camera.TakePicture()
    if ret:
        capture_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        print(f"Picture {i + 1} taken at {capture_time}")

        filename = f"picture_{capture_time}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Picture saved as {filename}")
    else:
        print("Warning: Failed to capture image")

print("Returning to Launch (RTL).")
dron.RTL()

print("Closing camera.")
camera.Close()

print("Mission complete!")
