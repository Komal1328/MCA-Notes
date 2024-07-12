from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Authenticates using local webserver
drive = GoogleDrive(gauth)

# File ID of the image you want to retrieve from Google Drive
file_id = '1y7jHyN4R7IGHWc2jRtCivKap_tgrhXTO'

# Retrieve the file
file = drive.CreateFile({'id': file_id})
file.GetContentFile('image.jpg')  # Save the file locally as 'image.jpg'
