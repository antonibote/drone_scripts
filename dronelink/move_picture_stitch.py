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

dron.fixHeading
print("Heading fixed")

dron.setMoveSpeed(1)
print(f"Speed set to {1} m/s")

images = []

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

        images.append(frame)
    else:
        print("Warning: Failed to capture image")

print("Returning to Launch (RTL).")
dron.RTL()

print("Closing camera.")
camera.Close()

if len(images) > 1:
    print("Stitching images together.")
    stitcher = cv2.Stitcher_create()
    status, stitched_image = stitcher.stitch(images)

    if status == cv2.Stitcher_OK:
        stitched_filename = "stitched_result.jpg"
        cv2.imwrite(stitched_filename, stitched_image)
        print(f"Stitched image saved as {stitched_filename}")
    else:
        print("Stitching failed.")
else:
    print("Not enough images to stitch.")

print("Mission complete!")
