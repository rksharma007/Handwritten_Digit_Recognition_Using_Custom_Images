# ----------------------------------------------------------------
# PROGRAM FOR PREPROCESSING THE DIGIT SAMPLES FROM CUSTOM DATASET
# Author - R K Sharma
# Github - https://github.com/rksharma007/
# ----------------------------------------------------------------

import glob
import math
import os

import cv2
import numpy as np
import PIL
from PIL import Image, ImageOps

#giving the path for loading and saving the images
save_path = "..\\task\\preprocessed_digits"
folder_path="..\\task\\custom_images\\*"

#preprocessing
for foldername in glob.glob(folder_path):                        #for all sub-directories in folder path
    for filename in glob.glob(foldername+'\\*.png'):             #for all .png files in sub-directories
        img = cv2.imread(filename)                               #read images using OpenCV
        crop = img[0:900, 150:1050]                              #cropping images to make square (1200*900 -> 900*900)
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)            #converting images to grayscale
        gray = cv2.resize(255-gray, (28,28))                     #inverting and resizing images to (28*28)
        (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #increasing the threshold of images

       #crop to bounding box
        while np.sum(gray[0]) == 0:
            gray = gray[1:]
        while np.sum(gray[:,0]) == 0:
            gray = np.delete(gray,0,1)
        while np.sum(gray[-1]) == 0:
            gray = gray[:-1]
        while np.sum(gray[:,-1]) == 0:
            gray = np.delete(gray,-1,1)
        rows,cols = gray.shape
        
        if rows > cols:
            factor = 20.0/rows
            rows = 20
            cols = int(round(cols*factor))
            gray = cv2.resize(gray, (cols,rows))
        else:
            factor = 20.0/cols
            cols = 20
            rows = int(round(rows*factor))
            gray = cv2.resize(gray, (cols, rows))

        #centering 
        colsPadding = (int(math.ceil((28-cols)/2.0)),int(math.floor((28-cols)/2.0)))
        rowsPadding = (int(math.ceil((28-rows)/2.0)),int(math.floor((28-rows)/2.0)))
        gray = np.lib.pad(gray,(rowsPadding,colsPadding),'constant')

        #saving preprocessed images into their respective folders
        if foldername == "..\\task\\train\\Sample001":
            cv2.imwrite(save_path+'\\0\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample002":
            cv2.imwrite(save_path+'\\1\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample003":
            cv2.imwrite(save_path+'\\2\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample004":
            cv2.imwrite(save_path+'\\3\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample005":
            cv2.imwrite(save_path+'\\4\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample006":
            cv2.imwrite(save_path+'\\5\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample007":
            cv2.imwrite(save_path+'\\6\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample008":
            cv2.imwrite(save_path+'\\7\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample009":
            cv2.imwrite(save_path+'\\8\\'+os.path.split(filename)[1], gray)
        if foldername == "..\\task\\train\\Sample010":
            cv2.imwrite(save_path+'\\9\\'+os.path.split(filename)[1], gray)
