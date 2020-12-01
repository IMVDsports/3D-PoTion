import cv2
import os
import numpy as np
from scipy.io import savemat
from scipy.io import loadmat

# script to convert JHMDB mat files (joint_positions) to a Penn Action mat file format

# I use INPUT_PATH to get class names and class video names
INPUT_PATH = "/usr/local/data01/julienbe/JHMDB_PA/frames/"

JOINT_POSTIONS = "/usr/local/data01/julienbe/JHMDBdataset/joint_positions/"
OUTPUT_PATH = "/usr/local/data01/julienbe/JHMDB_PA/labels3/"


count = 0
for filename in os.listdir(INPUT_PATH):
    ACTION = filename
    CLASS_PATH = ACTION + '/'

    for video in os.listdir(INPUT_PATH + CLASS_PATH):
        class_action = ACTION
        video_name = video
        nframes = len(os.listdir(INPUT_PATH + CLASS_PATH + video + '/'))
        frame0 = cv2.imread(INPUT_PATH + CLASS_PATH + video + '/' +'0.jpg')
        H, W, C = frame0.shape
        dimensions = [H, W, nframes]
        train = 1

        JHMDB_vid_annots = loadmat(JOINT_POSTIONS + CLASS_PATH + video + '/' + 'joint_positions.mat')
        pos_image = JHMDB_vid_annots["pos_img"] 
        JHMBD_x = pos_image[0,:,:]
        JHMBD_y = pos_image[1,:,:]
        PA_x = np.transpose(JHMBD_x)
        PA_y = np.transpose(JHMBD_y)

        formatedAnnots = {"action": class_action, "video_name": video_name, "x": PA_x, "y": PA_y, "train": train, "dimensions": dimensions, "nframes": nframes}
        savemat(OUTPUT_PATH +"%d.mat" % count, formatedAnnots)
        print("%d.mat" % count)
        count +=1