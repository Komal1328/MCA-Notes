import requests

# URL of the EAST text detector model
model_url = "https://github.com/opencv/opencv_extra/raw/master/testdata/dnn/frozen_east_text_detection.pb"

# Path where the model will be saved
model_path = "frozen_east_text_detection.pb"

# Download the model
print("[INFO] Downloading EAST text detector model...")
response = requests.get(model_url, stream=True)

# Save the model to disk
with open(model_path, "wb") as model_file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            model_file.write(chunk)

print(f"[INFO] Model downloaded and saved as {model_path}")
