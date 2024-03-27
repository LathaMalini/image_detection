# image_detection
This project implements object detection using the YOLOv8 model. It provides a Python script that performs object detection on images using pre-trained YOLOv8 weights and displays the results.

# Installation
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/object-detection.git
Install the required dependencies:
bash
Copy code
pip install opencv-python-headless ultralytics cvzone pandas
Download the YOLOv8 model weights file (yolov8s.pt) from the official Ultralytics repository and place it in the project directory.

Create a file named coco.txt containing the class labels for the COCO dataset. Each label should be on a separate line.

# Usage
Run the object detection script:
bash
Copy code
python object_detection.py
The script will process images located in the images/ directory.
Detected objects will be annotated with bounding boxes and class labels displayed on the images.
The script will print the count of each detected object class to the console.

# Project Structure
object_detection.py: Main Python script for performing object detection.
coco.txt: File containing COCO class labels.
images/: Directory containing input images for object detection.
yolov8s.pt: YOLOv8 model weights file.

# vedio of the project
https://github.com/LathaMalini/image_detection/assets/160328389/e4a7c3e1-977e-45c4-addf-c0bb2f57ede0

