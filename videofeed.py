import cv2
camera = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object to save the video

# ~ fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

video_writer = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))




while True:
        (grabbed, frame) = camera.read()  # grab the current frame
        
        frame = cv2.resize(frame, (640,480))        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       
        cv2.imshow("Frame", frame)  # show the frame to our screen
        cv2.imshow("Gray",gray)
        
  
        video_writer.write(gray)  # Write the video to the file system

        if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# cleanup the camera and close any open windows
camera.release()
video_writer.release()
cv2.destroyAllWindows()
