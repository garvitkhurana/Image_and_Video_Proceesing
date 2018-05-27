import cv2
import numpy as np

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]

px = img[55,55]
print(px)


# ~ It should be different now. Next, we can reference an ROI, or Region of Image, like so:

px = img[100:150,100:150]
print(px)


img[100:150,100:150] = [255,255,255]


watch_part=img[37:111,107:194]

img[0:74,0:87]=watch_part


print(img.shape)
print(img.size)
print(img.dtype)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
