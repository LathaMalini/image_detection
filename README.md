# image_detection
Download the YOLOv8 model weights file (yolov8s.pt) from the official Ultralytics repository and place it in the project directory.
Create a file named coco.txt containing the class labels for the COCO dataset. Each label should be on a separate line.
The script will iterate over images in the specified directory (images/) and perform object detection on each image.
Detected objects will be annotated with bounding boxes and labels displayed on the images.
The script will print the count of each detected object class to the console.

Project Structure
object_detection.py: Main script for performing object detection.
coco.txt: File containing COCO class labels.
images/: Directory containing input images for object detection.
yolov8s.pt: YOLOv8 model weights file.
