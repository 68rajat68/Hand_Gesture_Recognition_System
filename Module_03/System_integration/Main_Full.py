import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
import mouse
import threading
import numpy as np
import time
import pyautogui

pyautogui.FAILSAFE = False

frameR = 200
# Camera dimensions
cam_w, cam_h = 640, 480 
hSmall = 300

# Screen width and height used for mapping hand movements to screen coordinates.
screen_width, screen_height = pyautogui.size()

# Initialize the camera and set its width and height.
cap = cv2.VideoCapture(0)
cap.set(3, cam_w)
cap.set(4, cam_h)

# Initialize the hand detector with confidence level and max number of hands to detect.
detector = HandDetector(detectionCon=0.9, maxHands=1)   

l_pressed = False
r_pressed = False
double_pressed = False
up_pressed = False
down_pressed = False
volume_up = False
volume_down = False


# Delay variables used for ensuring actions (e.g., clicks) are not triggered too quickly

l_delay = 0
r_delay = 0
l_a_delay = 0
r_a_delay = 0
double_delay = 0

l_a_stop = False
r_a_stop = False


def l_clk_delay():
    global l_delay
    time.sleep(1)
    l_delay = 0


def r_clk_delay():
    global r_delay
    time.sleep(1)
    r_delay = 0
    

def double_clk_delay():
    global double_delay
    time.sleep(2)
    double_delay = 0


def l_a_clk_delay():
    global l_a_delay
    global l_a_stop
    while not l_a_stop:
        time.sleep(1)
        l_a_delay=0

def r_a_clk_delay():
    global r_a_delay
    global r_a_stop
    while not r_a_stop:
        time.sleep(1)
        r_a_delay=0


l_clk_thread = threading.Thread(target=l_clk_delay)
r_clk_thread = threading.Thread(target=r_clk_delay)
l_a_clk_thread = threading.Thread(target=l_a_clk_delay)
r_a_clk_thread = threading.Thread(target=r_a_clk_delay)
double_clk_thread = threading.Thread(target=double_clk_delay)


while True:
    success, img = cap.read()
    if success:
        img = cv2.flip(img, 1)
        hands, img = detector.findHands(img, flipType=False)
        cv2.rectangle(img, (frameR, 20), (cam_w - 20, cam_h - frameR + 40), (0, 145, 255), 2)

        if hands:
            lmlist = hands[0]['lmList'] 
            thumb_x,thumb_y=lmlist[4][0], lmlist[4][1]
            thumb_x3,thumb_y3=lmlist[3][0], lmlist[3][1]
            ind_d_x,ind_d_y=lmlist[5][0],lmlist[5][1]
            ind_x, ind_y = lmlist[8][0], lmlist[8][1]
            mid_x, mid_y = lmlist[12][0], lmlist[12][1]
            
            fingers = detector.fingersUp(hands[0])
            
            hand1=hands[0]
            centerX,centerY=hand1['center']
            
            # Mouse movement
            
            if centerX>frameR+40 and centerX<cam_w-40 and centerY>100 and centerY<cam_h-frameR + 80 :
                #Cursor point
                if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 1 and fingers[3] == 0 and fingers[4] == 0:
                    conv_x = int(np.interp(ind_x, (frameR+30, cam_w - 70), (0, screen_width)))
                    conv_y = int(np.interp(ind_y, (60, cam_h - frameR -30), (0, screen_height)))
                    mouse.move(conv_x, conv_y)

                # Mouse Button Clicks
                if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1 and fingers[3]==0:
                    # print(abs(ind_x - mid_x))
                    if abs(ind_x - mid_x) < 30:
                        # Left Click
                        if fingers[4] == 0 and fingers[1]==1 and fingers[2]==1  and fingers[3]==0 and l_delay == 0:
                            mouse.click(button="left")
                            l_delay = 1
                            if not l_clk_thread.is_alive():
                                l_clk_thread = threading.Thread(target=l_clk_delay)
                                l_clk_thread.start()
                                print("Left Click")
        
                        #right Click
                        if fingers[4] == 1 and fingers[1]==1 and fingers[2]==1  and fingers[3]==0 and r_delay == 0:
                            mouse.click(button = "right")
                            r_delay = 1
                            if not r_clk_thread.is_alive():
                                r_clk_thread = threading.Thread(target=r_clk_delay)
                                r_clk_thread.start()
                                print("Right Click")
                            

        aspect_ratio = img.shape[1] / img.shape[0]
        imgSmall = cv2.resize(img, ( int(hSmall * aspect_ratio), hSmall))

       
        cv2.imshow("CAMERA", imgSmall)
        cv2.moveWindow("CAMERA", screen_width - imgSmall.shape[1], 30)
        cv2.setWindowProperty("CAMERA", cv2.WND_PROP_TOPMOST, 1)
        
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()