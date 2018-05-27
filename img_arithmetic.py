import cv2
import numpy as np


# ~ img1=cv2.imread("im1.png")
# ~ img2=cv2.imread("im2.png")

img1=cv2.imread("im1.png")
img2=cv2.imread("logo.png")

# ~ add=img1+img2
# ~ pixel by pixel addition

# ~ add=cv2.add(img1,img2)

# ~ weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)


# ~ cv2.imshow('add',add)

# ~ cv2.imshow('add',weighted)


# I want to put logo on top-left corner, So I create a ROI


# ~ print(img2.shape)



rows,cols,channels = img2.shape

roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask




img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# add a threshold
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)


# ~ cv2.THRESH_BINARY
# ~ cv2.THRESH_BINARY_INV
# ~ cv2.THRESH_TRUNC
# ~ cv2.THRESH_TOZERO
# ~ cv2.THRESH_TOZERO_INV

mask_inv = cv2.bitwise_not(mask)


# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)






# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)





dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
