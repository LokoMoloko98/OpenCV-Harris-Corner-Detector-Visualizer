import numpy as np 
import cv2 as cv

#Import the input aerial image
filename = 'big ben london.jpg'
img = cv.imread(filename)

# convert the input image into grayscale color space 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# modify the data type setting to 32-bit floating point
gray = np.float32(gray)

imr = cv.resize(img, (750, 500)) 

# Display the Input Aerial Image before the cv.cornerHarris (Harris Corner Detector). 
cv.imshow('Input Image: The Elizabeth Tower (Big Ben), London, UK', imr)

# Apply the cv.cornerHarris method to detect the corners with appropriate values as input parameters.
dst = cv.cornerHarris(gray,2,3,0.04)

# Result is dilated for marking the corners.
dst = cv.dilate(dst, None)

# Reverting back to the original image, with optimal threshold value.
img[dst>0.01*dst.max()]=[0,0,255]
imr2 = cv.resize(img, (750, 500)) 
# Display the output of aerial image after applying the cv.cornerHarris 
cv.imshow('Output Harris Corner Detected Image: The Elizabeth Tower (Big Ben), London, UK', imr2)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()

    