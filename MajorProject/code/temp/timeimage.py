import cv2
import numpy as np
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import time
from vehicle_detector import VehicleDetector
import os


def image():
    # Load Vehicle Detector
    vd = VehicleDetector()

    # Choose one image path
    img_path = "images/1.jpg"

    output_folder = "output_images/"

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

    # Save the image with bounding boxes drawn
    img_name = os.path.basename(img_path)
    output_path = os.path.join(output_folder, img_name)
    cv2.imwrite(output_path, img)

    # Display the image with bounding boxes
    cv2.imshow("Vehicles", img)
    #cv2.waitKey(0)

    # Print the total number of vehicles in the image
    print("Total number of vehicles:", vehicle_count)

# RTSP URL
rtsp_url = 'rtsp://192.168.148.106:8554/mjpeg/1'
cv2.namedWindow("Live Transmission", cv2.WINDOW_AUTOSIZE)

count = 0

# Initialize Google Drive authentication
gauth = GoogleAuth()
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)

# Folder ID in Google Drive
folder_id = "1zxfStVA-kyV0xGGVTi18oau53iOVmyGv"


# Capture frames from RTSP stream
cap = cv2.VideoCapture(rtsp_url)

# Define the time interval (in seconds) between captures
capture_interval = 30
last_capture_time = time.time()

while True:
    # Read frame from the RTSP stream
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame from the RTSP stream.")
        break
    
    # Display frame
    cv2.imshow("Live Transmission", frame)
    
    # Check if it's time to capture a frame
    current_time = time.time()
    if current_time - last_capture_time >= capture_interval:
        count += 1
        filename = f"{count}.png"
        cv2.imwrite(filename, frame)
        print("Image saved as:", filename)

        test_images_folder = "test_images"
        if not os.path.exists(test_images_folder):
            os.makedirs(test_images_folder)
        test_image_path = os.path.join(test_images_folder, filename)
        if os.path.exists(test_image_path):
              os.remove(test_image_path)  # Remove existing file
        os.rename(filename, test_image_path)
        print("Image saved in 'test_images' folder.")
        
        if os.path.exists(test_image_path):
            print("File exists. Uploading to Google Drive...")

            # Upload image to Google Drive
            f = drive.CreateFile({'parents': [{'id': folder_id}], 'title': filename})
            f.SetContentFile(test_image_path)  # Use the correct file path
            f.Upload()
            print("Image uploaded to Google Drive.")
            print("Call image")
        else:
            print("Error: File not found. Unable to upload to Google Drive.")


        image()
        
        # Update the last capture time
        last_capture_time = current_time
    
    # Wait for key press
    key = cv2.waitKey(1)
    
    # Break loop when 'q' is pressed
    if key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
