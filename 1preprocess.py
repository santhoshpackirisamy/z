import cv2
from PIL import Image
import os, sys
import os,glob
from os import listdir,makedirs
from os.path import isfile,join
path = 'C:/Users/Acer/Desktop/SOURCE CODE/train/train' # Source Folder
dstpath = 'C:/Users/Acer/Desktop/SOURCE CODE/preprocess' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))]
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,gray)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil)
        image = cv2.resize(image,(256,256))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to greyscale
        cv2.imwrite(os.path.join(dstpath,fil),gray_image)
    except:
        print('{} is not converted')
        import numpy as np
        x=np.mean(img)
        print ('MEAN=',x)
        y=np.std(img)
        print('STANDARD DEVIATION=', y)
        z=np.var(img)
        print('VARIANCE=',z)
        break
