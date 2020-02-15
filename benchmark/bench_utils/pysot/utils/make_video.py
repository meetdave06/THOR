import numpy as np
import cv2
import os

class make_video:
    def __init__(self,video_path):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(os.path.join(video_path,"output.avi"), fourcc, 20.0, (1024,  1024))

    def write(self,frame):
        self.out.write(frame)

