import cv2
import os
from vehicle_detector import VehicleDetector


# Load Vehicle Detector
vd = VehicleDetector()

# Choose one image path
img_path = "images/4.png"

# Read the image
img = cv2.imread(img_path)

# Check if the image is empty or has invalid dimensions
if img is None or img.size == 0:
    print("Error: Unable to read the image or image has invalid dimensions.")
    exit()

# Detect vehicles in the image
vehicle_boxes = vd.detect_vehicles(img)
vehicle_count = len(vehicle_boxes)

# Draw bounding boxes
for box in vehicle_boxes:
    x, y, w, h = box
    cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
    cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

# Display the image with bounding boxes
cv2.imshow("Cars", img)
#cv2.waitKey(0)

# Print the total number of vehicles in the image
print("Total number of vehicles:", vehicle_count)
