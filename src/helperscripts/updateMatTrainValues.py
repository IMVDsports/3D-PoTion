import cv2
import os
import numpy as np
from scipy.io import savemat
from scipy.io import loadmat

#script to split dataset (by updating annotations["train"] to 2 if it belongs to test set)
# script parses over split.txt files provided in JHMDB dataset

INPUT_PATH = "/usr/local/data01/julienbe/JHMDB_PA/frames/"
SPLITS = "/usr/local/data01/julienbe/JHMDBdataset/splits/"
LABELS_PATH = "/usr/local/data01/julienbe/JHMDB_PA/labels2processed/"

# SPLIT_FILE = open(SPLITS + "brush_hair_test_split1.txt","r")

#create a list of videos to put in Test set
ListToTest = []
for filename in os.listdir(INPUT_PATH):

    ACTION = filename
    SPLIT_FILE = open(SPLITS + ACTION+"_test_split1.txt","r")
    all_lines = SPLIT_FILE.readlines()

    for curr_line in all_lines:
        words = curr_line.split(" ")
        if (int(words[1])==2):
            ListToTest.append(words[0].split(".")[0])

    print(len(ListToTest))



count = 1
# update the mat files corresponding to the videos in this list. (annotations["train"] to 2)
for filename in os.listdir(LABELS_PATH):
    if filename.endswith(".mat"):
        print(filename)
        annotations1 = loadmat(LABELS_PATH + filename)
        video_name1 = annotations1["video_name"]

        for NAME in ListToTest:
            if(NAME==video_name1):
                action1 = annotations1["action"]
                nframes1 = annotations1["nframes"]
                dimensions1 = annotations1["dimensions"]
                x1 = annotations1["x"] 
                y1 = annotations1["y"] 
                train2 = 2
                annotations2 = {"action": action1, "video_name": video_name1, "x": x1, "y": y1, "train": train2, "dimensions": dimensions1, "nframes": nframes1} 
                savemat(LABELS_PATH + filename, annotations2)
                print("UPDATE = ", count)
                count += 1