# import the necessary packages
import numpy as np
import argparse
import cv2
import imutils

# construct arg parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', type=str, default='z.jpg',
    help='path to the input image')
args = vars(ap.parse_args())

# load the original input image and display it to our screen
image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)

# a mask is the same size as our image, but has only two pixel
# values, 0 and 255 -- pixels with a value of 0 (background) are
# ignored in the original image while mask pixels with a value of
# 255 (foreground) are allowed to be kept
mask = np.zeros(image.shape[:2], dtype="uint8")
#cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)
cv2.rectangle(mask, (225, 175), (750, 500), 255, -1)
cv2.imshow("Rectangular Mask", mask)

# apply our mask -- notice how only the person in the image is
# cropped out
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Write image to disk
#cv2.imwrite('some...filename', masked)