import os
import math

images = os.listdir(os.path.join('second-dataset','Train','images'))
labels = os.listdir(os.path.join('second-dataset', 'Train', 'labels'))

train_images = images[:35800]
val_images = images[35800:]

train_labels =  labels[:35800]
val_labels = labels[35800:]




print(len(train_images), len(val_images), len(train_labels), len(val_labels))

for image in train_images:
    os.rename(os.path.join('second-dataset','Train','images', image), r"C:\Users\Ethan\Desktop\code\weapondetection\yolov7\data\second-dataset\train\images"+image)

for image in val_images:
    os.rename(os.path.join('second-dataset','Train','images', image), r"C:\Users\Ethan\Desktop\code\weapondetection\yolov7\data\second-dataset\val\images"+image)

for label in train_labels: 
    os.rename(os.path.join('second-dataset', 'Train', 'labels', label), r"C:\Users\Ethan\Desktop\code\weapondetection\yolov7\data\second-dataset\train\labels"+label)

for label in val_labels:
    os.rename(os.path.join('second-dataset', 'Train', 'labels', label), r"C:\Users\Ethan\Desktop\code\weapondetection\yolov7\data\second-dataset\val\labels"+label)