import cv2 
import os


#script to convert .avi JHMDB videos to a list of frames. 

VIDEO_PATH = "/usr/local/data01/julienbe/JHMDBdataset/ReCompress_Videos/"
VIDEO_CLASS = "wave/"
FRAME_PATH = "/usr/local/data01/julienbe/JHMDB_PA/frames/"
FRAME_CLASS = "wave/"

os.system('mkdir ' + FRAME_PATH + FRAME_CLASS)

for filename in os.listdir(VIDEO_PATH + VIDEO_CLASS):
    if filename.endswith(".avi"): 
        vidcap = cv2.VideoCapture(VIDEO_PATH + VIDEO_CLASS + filename)
        success,image = vidcap.read()
        count = 0
        video_folder = FRAME_PATH + FRAME_CLASS + os.path.splitext(filename)[0] +"/"
        os.system('mkdir ' + video_folder)
        while success:
            cv2.imwrite(video_folder +"%d.jpg" % count, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            count += 1

