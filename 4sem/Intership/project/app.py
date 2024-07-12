from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import cv2
import numpy as np

app = Flask(__name__)

# Configuration for YOLO
whT = 320
confThreshold = 0.5
nmsThreshold = 0.3
modelConfig = 'yolov3.cfg'
modelWeights = 'yolov3.weights'
classesfile = 'coco.names'

# Load the class names
classNames = []
with open(classesfile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load the network
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

    detected_objects = []
    if len(indices) > 0:
        for i in indices.flatten():  # Use flatten to handle the indices correctly
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i] * 100)}%', 
                        (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
            detected_objects.append({
                'class': classNames[classIds[i]],
                'confidence': confs[i],
                'bbox': [x, y, w, h]
            })
    return detected_objects

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_objects():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image found'})

        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({'error': 'No image selected'})

        image_path = os.path.join('uploads', image_file.filename)
        image_file.save(image_path)

        # Read the image
        img = cv2.imread(image_path)
        if img is None:
            return jsonify({'error': 'Invalid image file'})

        # Use the original image size for detection
        blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
        net.setInput(blob)
        layerNames = net.getLayerNames()
        outputNames = [layerNames[i - 1] for i in net.getUnconnectedOutLayers()]

        outputs = net.forward(outputNames)

        detected_objects = findObject(outputs, img)

        # Save the output image in the output folder
        output_folder = 'output'
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, image_file.filename)
        cv2.imwrite(output_path, img)

        return jsonify({'image_path': output_path, 'objects': detected_objects})

    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route('/output/<filename>')
def output_file(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('output', exist_ok=True)
    app.run(debug=True)
