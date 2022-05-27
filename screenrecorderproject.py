import cv2
import numpy as np
import pyautogui

#screen resolution using pyautogui
SCREEN_SIZE = tuple(pyautogui.size())

fourcc = cv2.VideoWriter_fourcc(*"XVID")
# frames per second
fps = 12.0
# create the video write object
file_name = f'{input("ENTER FILE NAME")}.mp4'
out = cv2.VideoWriter(file_name, fourcc, fps, (SCREEN_SIZE))
# the time you want to record in seconds
record_seconds = 200

for i in range(int(record_seconds * fps)):
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # writing the frame
    out.write(frame)
    # showing the frame
    cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    if cv2.waitKey(1) == ord("q"):
        break


cv2.destroyAllWindows()
out.release()

