import pyautogui
import cv2
import numpy as np

#Specify Resolution
resolution = (1920, 1080)

#Specify Video Codec
codec = cv2.VideoWriter_sourcc(*"XVID")

#Specify name of Output file
filename = "Recording.avi"

#Specify frames rate. We can choose any value and experiment with it
fps = 60.0

#Creating a VideoWriter object
out = cv2.VideoWriter_sourcc(filename, codec, fps, resolution)

#Create an Empty Window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

#Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    #Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    #Convert the screenshot to a numpy array
    frame = np.array(img)

    #Convert it from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Write it to the output file
    out.write(frame)

    #Optional: Display the recording screen
    cv2.imshow('Live', frame)

    #Stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

#Release the Video Writer
out.release()

#Destroy all the Windows
cv2.destroyAllWindows()