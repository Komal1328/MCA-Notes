import cv2
import numpy as np
import time
from vehicle_detector import VehicleDetector
import os
import mysql.connector
from mysql.connector import Error
import datetime
import os

#Establish database connection

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='smartflow',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

#create table

def create_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS traffic_images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        image LONGBLOB NOT NULL,
        date DATE NOT NULL,
        time TIME NOT NULL,
        extension VARCHAR(5) NOT NULL
    )
    """
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()

# insert image  to data abse

def insert_image(connection, image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    cursor = connection.cursor()
    with open(image_path, 'rb') as file:
        binary_data = file.read()
    
    date_today = datetime.date.today()
    time_now = datetime.datetime.now().time()
    extension = os.path.splitext(image_path)[1][1:]  # Get the file extension without the dot
    
    # Insert the image and get the inserted ID
    insert_query = """
    INSERT INTO traffic_images (image, date, time, extension)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (binary_data, date_today, time_now, extension))
    connection.commit()
    image_id = cursor.lastrowid  # Get the ID of the inserted row

    # Update the image name with the ID
    image_name = f"{image_id}.{extension}"
    update_query = """
    UPDATE traffic_images
    SET name = %s
    WHERE id = %s
    """
    cursor.execute(update_query, (image_name, image_id))
    connection.commit()

    cursor.close()
    print(f"Image inserted successfully with ID {image_id} and name {image_name}")


# retrive image from database

def retrieve_recent_image(connection, save_path):
    cursor = connection.cursor()
    select_query = "SELECT name, image, extension FROM traffic_images ORDER BY id DESC LIMIT 1"
    cursor.execute(select_query)
    record = cursor.fetchone()
    if record:
        name, image_data, extension = record
        file_name = f"{name}"
        file_path = os.path.join(save_path, file_name)
        with open(file_path, 'wb') as file:
            file.write(image_data)
        print(f"Most recent image {file_name} saved to {save_path}")
        cursor.close()
        return file_path
    else:
        print("No images found")
        cursor.close()
        return None


# detect number of vehicles

def congestion(img_path):

    print("Image")
    # Load Vehicle Detector
    vd = VehicleDetector()

    # Choose one image path
    #img_path = "images/1.jpg"

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
    print("Total number of vehicles in a lane:", vehicle_count)


def image1():
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

    return vehicle_count

#-------------------------------------------------------------------------------

# Directory where you want to save the image
save_directory = r"C:\Users\ASUS\Desktop\source code\Downloads"

# Ensure the save directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

cap = cv2.VideoCapture('rtsp://192.168.224.19:8554/mjpeg/1')  
if not cap.isOpened():
    print("Error: Unable to open RTSP stream")
    exit()

speed = 10

capture_interval = 10  # Time interval in seconds to capture a frame
last_capture_time = time.time()
count = 0

connection = create_connection()
if connection:
    create_table(connection)
else:
    print("Error: Unable to connect to the database")
    exit()

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
            print("File exists. Uploading to database...")
            insert_image(connection, test_image_path)
        else:
            print("Error: File not found. Unable to upload to database.")

        recent_image_path = retrieve_recent_image(connection, save_directory)
        if recent_image_path:
            congestion(recent_image_path)
        
        vehicle_count=image1()
        green_dealy = vehicle_count * speed
        print("speed:",green_dealy)


        # Update the last capture time
        last_capture_time = current_time
    
    # Wait for key press
    key = cv2.waitKey(1)
    
    # Break loop when 'q' is pressed
    if key == ord('q'):
        break

# Retrieve the most recent image and save it
retrieve_recent_image(connection, save_directory)

# Release resources
cap.release()
cv2.destroyAllWindows()
if connection:
    connection.close()
