import mysql.connector
import requests
import os

# Database connection parameters
host = "lms.pptik.id"  # Often this is 'localhost' or an IP address
database = "moodle"  # Your Moodle database name
user = "adminmoodle"
password = "Pptik2023!"

# Establishing the connection
conn = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

print (f"connection status: {conn.is_connected}")
# Creating a cursor object to interact with the database
cursor = conn.cursor()

# Example query
query = "SELECT faceimage FROM mdl_proctoring_face_images WHERE facefound = '1';"  # Replace with your actual query
cursor.execute(query)

# Directory to save images
image_dir = "D:/python-rmq/proc-images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Downloading and saving images
for (image_url,) in cursor:
    '''
    if len(row) == 2:  # Check if the row has two elements
        image_url, facefound = row
    '''
    if image_url:
        # Making a request to the image URL
        response = requests.get(image_url)
        print (f"response status: {response}")
        if response.status_code == 200:
            # Extracting image filename from URL
            filename = image_url.split('/')[-1]
            filepath = os.path.join(image_dir, filename)

            # Saving the image
            with open(filepath, 'wb') as file:
                file.write(response.content)
                print ('image saved')

# Closing the connection
cursor.close()
conn.close()
