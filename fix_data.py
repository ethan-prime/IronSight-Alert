import os

for file in os.listdir(os.path.join('yolov7', 'data', 'val', 'labels')):
    os.rename(os.path.join('yolov7', 'data', 'val', 'labels', file), os.path.join('yolov7', 'data', 'val', 'labels', file+'.txt'))