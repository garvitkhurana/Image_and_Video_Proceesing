import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,130,130])
    upper_red = np.array([255,255,255])
    
    # ~ for gray
    # ~ lower_gray = np.array([0,0,0])
    # ~ upper_gray = np.array([120,40,200])
    
  # ~ Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
        
cv2.destroyAllWindows()
cap.release()
'''
green = np.uint8([[[0,0,255]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)

'''
