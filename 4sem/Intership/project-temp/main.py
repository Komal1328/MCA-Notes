import cv2
import numpy as np
import os

# Path to the folder containing images
image_folder = r'C:\Users\ASUS\Desktop\Intership\project\images'
output_folder = r'C:\Users\ASUS\Desktop\Intership\project\output'

whT = 320
confThreshold = 0.5
nmsThreshold = 0.3

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load the class names
classesfile = 'coco.names'
classNames = []
with open(classesfile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load the model configuration and weights
modelConfig = 'yolov3.cfg'
modelWeights = 'yolov3.weights'
net = cv2.dnn.readNetFromDarknet(modelConfig, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def findObject(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w, h = int(det[2] * wT), int(det[3] * hT)
                x, y = int((det[0] * wT) - w / 2), int((det[1] * hT) - h / 2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))

    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)

    if len(indices) > 0:
        for i in indices:
            #i = i[0]  # Access the index inside the list
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
    else:
        print("No objects detected in the image.")

# Loop through each image in the folder
for filename in os.listdir(image_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img_path = os.path.join(image_folder, filename)
        img = cv2.imread(img_path)

        # Use the original image size for detection
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        layerNames = net.getLayerNames()
        outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]

        outputs = net.forward(outputNames)

        findObject(outputs, img)

        # Save the output image in the output folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, img)

        # Display the image
        cv2.imshow('Image', img)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
