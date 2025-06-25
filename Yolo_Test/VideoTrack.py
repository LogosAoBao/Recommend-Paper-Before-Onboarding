from ultralytics import YOLO

# Load a model
#model = YOLO("yolo11n.pt")  # load an official detection model
#model = YOLO("yolo11n-seg.pt")  # load an official segmentation model
model = YOLO("../runs/detect/train7/weights/best.pt")  # load a custom model

# Track with the model
##results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True)
#results = model.track(source="https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")
results = model.track(source="https://www.bilibili.com/video/BV1RRK5zYEoK", show=True, tracker="bytetrack.yaml")