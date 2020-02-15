import numpy as np
import cv2
import os

class make_video:
    def __init__(self,video_path,im_width,im_height):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(os.path.join(video_path,"output.avi"), fourcc, 20.0, (im_width, im_height))

    def write(self,frame):
        self.out.write(frame)

