import mysql.connector
from mysql.connector import Error
import datetime
import os

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='smartflow',  # Replace with your database name
            user='root',           # Replace with your MySQL username
            password=''            # Replace with your MySQL password
        )
        if connection.is_connected():
            print("Connection to MySQL database was successful")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

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

def insert_image(connection, name, image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    
    cursor = connection.cursor()
    with open(image_path, 'rb') as file:
        binary_data = file.read()
    
    date_today = datetime.date.today()
    time_now = datetime.datetime.now().time()
    extension = os.path.splitext(image_path)[1][1:]  # Get the file extension without the dot
    
    insert_query = """
    INSERT INTO traffic_images (name, image, date, time, extension)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (name, binary_data, date_today, time_now, extension))
    connection.commit()
    print("Image inserted successfully")

def retrieve_recent_image(connection, save_path):
    cursor = connection.cursor()
    select_query = "SELECT name, image, extension FROM traffic_images ORDER BY id DESC LIMIT 1"
    cursor.execute(select_query)
    record = cursor.fetchone()
    if record:
        name, image_data, extension = record
        file_name = f"{name}.{extension}"
        file_path = os.path.join(save_path, file_name)
        with open(file_path, 'wb') as file:
            file.write(image_data)
        print(f"Most recent image {file_name} saved to {save_path}")
    else:
        print("No images found")

# Directory where you want to save the image
save_directory = r"C:\Users\ASUS\Desktop\source code\Downloads"

# Ensure the save directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

connection = create_connection()
if connection:
    create_table(connection)
    insert_image(connection, 'Traffic Image', r"C:\Users\ASUS\Desktop\Emergency-Vehicle-Detection-master\images\2.jpg")  # Replace with your actual image path
    retrieve_recent_image(connection, save_directory)
    connection.close()
