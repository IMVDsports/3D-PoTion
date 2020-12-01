import cv2
import os
import numpy as np
from scipy.io import savemat
from scipy.io import loadmat

#script to put locations of hidden joints, i.e. joint locations out of the frame boundaries, to (x,y) = (0,0)

INPUT_PATH = "/usr/local/data01/julienbe/JHMDB_PA/labels2/"
OUTPUT_PATH = "/usr/local/data01/julienbe/JHMDB_PA/labels2processed/"

for filename in os.listdir(INPUT_PATH):
    if filename.endswith(".mat"):
        print(filename)
        annotations1 = loadmat(INPUT_PATH + filename)

        action1 = annotations1["action"]
        video_name1 = annotations1["video_name"]
        train1 = annotations1["train"]
        nframes1 = annotations1["nframes"]
        dimensions1 = annotations1["dimensions"]
        MAX_X = annotations1["dimensions"][0][0]
        MAX_Y = annotations1["dimensions"][0][1]
        x1 = annotations1["x"] 
        y1 = annotations1["y"] 
        x2 = x1
        y2 = y1
        x_height, x_width = annotations1['x'].shape
        for i in range(x_height):
            for j in range(x_width):
                if(int(x1[i,j])>MAX_X):
                    x2[i,j]=0.0
        y_height, y_width = annotations1['y'].shape
        for i in range(y_height):
            for j in range(y_width):
                if(int(y1[i,j])>MAX_Y):
                    y2[i,j]=0.0

        annotations2 = {"action": action1, "video_name": video_name1, "x": x2, "y": y2, "train": train1, "dimensions": dimensions1, "nframes": nframes1} 
        savemat(OUTPUT_PATH + filename, annotations2)