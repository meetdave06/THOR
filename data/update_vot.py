import json
import pathlib
import shutil
import os
import cv2

filename = "VOT2019.json"
with open(filename, 'r') as f:
    vot_dict = json.load(f)


for key in list(vot_dict):
    for dir in list(vot_dict[key]):
        if dir=="img_names":
            for i,img_name in  enumerate(vot_dict[key][dir]):
                first_image = cv2.imread("VOT2019/"+img_name)
                height, width = first_image.shape[0], first_image.shape[1]
                break
            vot_dict[key]['height'] = height
            vot_dict[key]['width'] = width


with open("VOT2019.json", 'w') as f:
    json.dump(vot_dict, f)

