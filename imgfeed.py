
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('watch.jpg',0)

# ~ 0 for IMREAD_GRAYSCALE
# ~ other options are IMREAD_COLOUR=1
# ~ AND IMREAD_UNCHHANGED=-1


# ~ using cv2

# ~ img = cv2.imread('hol.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# ~ using plt


# ~ plt.imshow(img,cmap='gray',interpolation='bicubic')

# ~ to plot


# ~ plt.plot([330,10],[500,800],'r',linewidth=13)


# ~ plt.show()


# ~ to save

# ~ cv2.imwrite('image new name.format',img)
