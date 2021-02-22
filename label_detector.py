# imports
import cv2
import numpy as np

# adjusting size of image for now may be changed later
path = 'Images/image.jpg'
src = cv2.imread(path)
scale_percent = 20

#adjusting width
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# adjusting output size
dsize = (width, height)

output = cv2.resize(src,dsize)
# writing new image to look at
cv2.imwrite('./Images/scaled_image.png', output)

path = 'Images/scaled_image.png'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

#creating our classes
classNames= []
classFile = 'open_cv_resources/classes.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
print(classNames)

cv2.imshow('Original', img)
cv2.imshow('Original', imgGray)


cv2.waitKey(0)
