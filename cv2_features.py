

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('watch.jpg',1)

cv2.line(img,(0,0),(150,150),(255,255,255),15,cv2.LINE_AA)

cv2.rectangle(img,(30,50),(550,450),(255,0,255),15)

cv2.circle(img,(100,63), 55, (0,255,0), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)

# OpenCV documentation had this code, which reshapes the array to a 1 x 2. I did not 
# find this necessary, but you may:
#pts = pts.reshape((-1,1,2))


cv2.polylines(img, [pts], True, (0,255,255), 3)

cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

# ~ Python: cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])


# ~ Type of the line:

# ~ 8 (or omitted) - 8-connected line.
# ~ 4 - 4-connected line.
# ~ cv2.LINE_AA - antialiased line.




cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
