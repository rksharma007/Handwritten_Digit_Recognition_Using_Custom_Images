import glob
import os

import PIL
from PIL import Image, ImageOps

path = "C:\\Users\\theycallmeBOT\\Desktop\\task\\cropped_digits_samples"
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
    
img_path="C:\\Users\\theycallmeBOT\\Desktop\\task\\UAS_train_images\\*.png"
for filename in glob.glob(img_path):
    img = Image.open(filename)
    border = (150, 0, 150, 0) # left, top, right, bottom
    img = ImageOps.crop(img, border)
    img.save('{}{}{}'.format(path,'\\',os.path.split(filename)[1]))
