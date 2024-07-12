# Import necessary packages
from imutils.object_detection import non_max_suppression
import numpy as np
import pytesseract
import imutils
import cv2

# Configuration for Tesseract OCR engine path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def decode_predictions(scores, geometry):
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidences = []

    for y in range(0, numRows):
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]

        for x in range(0, numCols):
            if scoresData[x] < 0.5:
                continue

            (offsetX, offsetY) = (x * 4.0, y * 4.0)
            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)
            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]
            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)
            rects.append((startX, startY, endX, endY))
            confidences.append(scoresData[x])

    return (rects, confidences)

# Fixed parameters
image_path = r"C:\Users\ASUS\Desktop\images\3.jpg"
east_model_path = r"C:\Users\ASUS\Desktop\Emergency-Vehicle-Detection-master\frozen_east_text_detection.pb"

min_confidence = 0.5
width = 320
height = 320
padding = 0.05

print("[INFO] loading EAST text detector...")
net = cv2.dnn.readNet(east_model_path)

image = cv2.imread(image_path)
orig = image.copy()
(origH, origW) = image.shape[:2]

newW, newH = width, height
rW = origW / float(newW)
rH = origH / float(newH)

image = cv2.resize(image, (newW, newH))
(H, W) = image.shape[:2]

blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)
net.setInput(blob)
(scores, geometry) = net.forward(["feature_fusion/Conv_7/Sigmoid", "feature_fusion/concat_3"])

(rects, confidences) = decode_predictions(scores, geometry)
boxes = non_max_suppression(np.array(rects), probs=confidences)

results = []

for (startX, startY, endX, endY) in boxes:
    startX = int(startX * rW)
    startY = int(startY * rH)
    endX = int(endX * rW)
    endY = int(endY * rH)

    dX = int((endX - startX) * padding)
    dY = int((endY - startY) * padding)

    startX = max(0, startX - dX)
    startY = max(0, startY - dY)
    endX = min(origW, endX + (dX * 2))
    endY = min(origH, endY + (dY * 2))

    roi = orig[startY:endY, startX:endX]
    config = ("-l eng --oem 1 --psm 7")
    text = pytesseract.image_to_string(roi, config=config)
    results.append(((startX, startY, endX, endY), text))

results = sorted(results, key=lambda r: r[0][1])

for ((startX, startY, endX, endY), text) in results:
    print("OCR TEXT")
    print("========")
    print("{}\n".format(text))
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    output = orig.copy()
    cv2.rectangle(output, (startX, startY), (endX, endY), (0, 0, 255), 2)
    cv2.putText(output, text, (startX, startY - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.imshow("Text Detection", output)

    if "AMBULANCE" in text:
        print("AMBULANCE detected. Stopping further processing.")
        output_image_path = r"C:\Users\ASUS\Desktop\source code\Output\output_images\output.jpg"
        cv2.imwrite(output_image_path, output)
        break

cv2.waitKey(0)
cv2.destroyAllWindows()