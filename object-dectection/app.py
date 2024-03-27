from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import pandas as pd
from collections import Counter
from ultralytics import YOLO
import cvzone
import glob
import os

app = Flask(__name__)

model = YOLO("yolov8s.pt")

# Load class list
with open(r"C:\Users\hp\Downloads\yolov8-object-count-in-image-main\yolov8-object-count-in-image-main\coco.txt", "r") as f:
    class_list = f.read().split("\n")





def object_detection(img):
    results = model.predict(img)
    print(results)  # Print results object for inspection
    if not results:
        return img, []

    object_classes = []
    for result in results:  # Iterate over results directly
        if len(result) < 6:  # Check if result has fewer than 6 values
            continue  # Skip processing if result doesn't have enough values

        # Convert boxes to NumPy array
        boxes_np = result.boxes.numpy()
        boxes = boxes_np[:, :4].tolist()  # Extract bounding box coordinates

        for box in boxes:
            x1, y1, x2, y2 = map(int, box)
            obj_class = class_list[int(result.names[int(result.probs.argmax(dim=-1))])]
            object_classes.append(obj_class)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)

    return img, object_classes




def count_objects(object_classes):
    counter = Counter(object_classes)
    return counter

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        # Save uploaded file
        file_path = os.path.join('uploads',file.filename )
        file.save(file_path)

        # Perform object detection
        img = cv2.imread(file_path)
        img = cv2.resize(img, (1020, 500))
        img, object_classes = object_detection(img)
        counts = count_objects(object_classes)

        # Display result
        result_image_path = '/static/C:/Users/hp/Downloads/yolov8-object-count-in-image-main/yolov8-object-count-in-image-main/images'

        cv2.imwrite('/static/C:/Users/hp/Downloads/yolov8-object-count-in-image-main/yolov8-object-count-in-image-main/images', img)
        return render_template('index.html', image=result_image_path, counts=counts)


if __name__ == '__main__':
    # Ensure 'uploads' folder exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
