import cv2
import os
import glob
from vehicle_detector import VehicleDetector


# Load Vehicle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder = glob.glob("images/*.jpg")

# Output folder
output_folder = "output_images/"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

vehicles_folder_count = 0

# Loop through all the images
for img_path in images_folder:
    print("Img path", img_path)
    img = cv2.imread(img_path)

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # Update total count
    vehicles_folder_count += vehicle_count

    # Draw bounding boxes
    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)
        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

    # Save the image with bounding boxes drawn
    img_name = os.path.basename(img_path)
    output_path = os.path.join(output_folder, img_name)
    cv2.imwrite(output_path, img)

    # Display the image with bounding boxes
    cv2.imshow("Cars", img)
    cv2.waitKey(0)  # Wait for any key press before showing the next image

    # Print the total number of vehicles in the current image
    print("Total number of vehicles:", vehicle_count)

print("Total current count", vehicles_folder_count)
