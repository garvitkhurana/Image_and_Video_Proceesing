import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()
    frame=cv2.resize(frame,(240,360))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,130,130])
    upper_red = np.array([255,255,255])
    
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    
    
    kernel = np.ones((5,5),np.float32)/25
    
    smoothed = cv2.filter2D(res,-1,kernel)
    
    
    bilateral = cv2.bilateralFilter(res,15,100,50)
    
    median = cv2.medianBlur(res,15)
    
    blur = cv2.GaussianBlur(res,(15,15),0)
    
    norm=cv2.blur(res,(15,15))
    
    
    cv2.imshow('Original',frame)
    # ~ cv2.imshow('Median Blur',median)
    cv2.imshow('bilateral Blur',bilateral)
    # ~ cv2.imshow('Gaussian Blurring',blur)
    # ~ cv2.imshow('Averaging',smoothed)
    cv2.imshow('Normal CV2 filter',norm)


    if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()
