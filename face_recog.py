#face_recognition app
#uses openCV
#use cv2. (in console to look at available things)
#dir(x) x is string
#using https://realpython.com/face-recognition-with-python/


import cv2
import os

dir = "path/to/directory"
# get a list of all the files in "dir" that don't start with "."
valid_files = [file for file in os.listdir(dir) if not file.startswith('.')]

for file in valid_files:
    # get the full filepath
    filepath = os.path.join(dir, file)
