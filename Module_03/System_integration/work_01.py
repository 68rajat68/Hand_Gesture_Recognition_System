import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
import mouse
import threading
import numpy as np
import time
import pyautogui
import math

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



# Initialize dragging state
dragging = False

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
            ind_d_x,ind_d_y=lmlist[8][0],lmlist[8][1]
            ind_x, ind_y, ind_z = lmlist[5][0], lmlist[5][1], lmlist[5][2]
            mid_x, mid_y,mid_z = lmlist[12][0], lmlist[12][1], lmlist[12][2]
            wrist_x1, wrist_y1, wrist_z1 = lmlist[0][0], lmlist[0][1], lmlist[0][2]
            wrist_x2, wrist_y2, wrist_z2 = lmlist[9][0], lmlist[9][1], lmlist[9][2]
            
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
                
                
                # Mouse Scrolling
                if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0  and fingers[3] == 0 and fingers[4] == 0:
                    if abs(ind_x - mid_x) < 25:
                        mouse.wheel(delta=-1)
                    # print(math.sqrt((mid_x - ind_x) ** 2 + (mid_y - ind_y) ** 2))
                    # print(abs(ind_x - mid_x))
                    # if (math.sqrt((mid_x - ind_x) ** 2 + (mid_y - ind_y) ** 2) < 110):
                    #     mouse.wheel(delta=-1)
                if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 0 and fingers[3] == 0 and fingers[4] == 1:
                    if abs(ind_x - mid_x) < 25:
                        mouse.wheel(delta=1)
                    # print(abs(ind_x - mid_x))
                    # print(math.sqrt((mid_x - ind_x) ** 2 + (mid_y - ind_y) ** 2))
                    # if (math.sqrt((mid_x - ind_x) ** 2 + (mid_y - ind_y) ** 2) < 110):
                    #     mouse.wheel(delta=1)
                
                
                # Mouse text selection
                if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 0 and fingers[3] == 0 and fingers[4] == 0:
                    # Check if the thumb and index finger are close enough to start dragging
                    if abs(ind_x - thumb_x3) < 30:
                        if not dragging:
                            dragging = True
                            print("Start dragging - Thumb and Index are close.")
                            pyautogui.mouseDown()  # Start dragging
                            
                        # If already dragging, continue moving the mouse
                        if dragging:
                            # Map index finger coordinates to screen coordinates
                            conv_x = int(np.interp(ind_x, (frameR+30, cam_w - 70), (0, screen_width)))
                            conv_y = int(np.interp(ind_y, (60, cam_h - frameR - 30), (0, screen_height)))
                            pyautogui.moveTo(conv_x, conv_y)

                    # If thumb is not close to index, stop dragging
                    else:
                        if dragging:
                            dragging = False
                            print("Stop dragging - Thumb moved away.")
                            pyautogui.mouseUp()  # End dragging

                # If gesture changes (not a dragging gesture), ensure mouse is up
                else:
                    if dragging:
                        pyautogui.mouseUp()
                        dragging = False
                        print("Gesture changed - Ensuring drag is stopped.")
                
                
                # right and left click
                if fingers[1] == 1 and fingers[2] == 1 and fingers[0] == 1 and fingers[3]==0:
                    # print(abs(ind_x - mid_x))
                    if abs(ind_x - mid_x) < 30:
                        # Left Click
                        if fingers[4] == 0 and fingers[1]==1 and fingers[2]==1  and fingers[3]==0 and l_delay == 0:
                            mouse.click(button="left")
                            print("Left Click")
                            l_delay = 1
                            if not l_clk_thread.is_alive():
                                l_clk_thread = threading.Thread(target=l_clk_delay)
                                l_clk_thread.start()
        
                        #right Click
                        if fingers[4] == 1 and fingers[1]==1 and fingers[2]==1  and fingers[3]==0 and r_delay == 0:
                            mouse.click(button = "right")
                            print("Right Click")
                            r_delay = 1
                            if not r_clk_thread.is_alive():
                                r_clk_thread = threading.Thread(target=r_clk_delay)
                                r_clk_thread.start()
                
                # Keyboard Arrow Control 
                if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 and l_a_delay == 0:
                    keyboard.press('left')
                    print("Left Arrow Button Clicked")
                    l_a_delay=1
                    if not l_a_clk_thread.is_alive():
                        l_a_stop =False
                        l_a_clk_thread = threading.Thread(target=l_a_clk_delay)
                        l_a_clk_thread.start()
                    keyboard.release('left')
                    
                elif fingers[4] == 1 and fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and r_a_delay == 0:
                    keyboard.press('right')
                    print("Right Arrow Button Clicked")
                    r_a_delay=1
                    if not r_a_clk_thread.is_alive():
                        r_a_stop =False
                        r_a_clk_thread = threading.Thread(target=r_a_clk_delay)
                        r_a_clk_thread.start()
                    keyboard.release('right')
                    
                elif not(fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0 ) and not(fingers[4] == 1 and fingers[0] == 1 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0):
                    if r_a_clk_thread.is_alive():
                        r_a_delay = 0
                        r_a_stop =True
                    if l_a_clk_thread.is_alive():
                        l_a_delay = 0
                        l_a_stop =True
                
                
                
                #Volume UP and Down
                dis = ((ind_x-thumb_x)**2 + (ind_y-thumb_y)**2)**(0.5)   
                
                if fingers == [0,1,1,1,1] :
                    cv2.circle(img,center=(ind_d_x,ind_d_y),radius=10,color=(0,150,255),thickness=2)
                    cv2.circle(img,center=(thumb_x,thumb_y),radius=10,color=(0,150,255),thickness=2)
                    
                    if(dis > 75 ):
                        cv2.line(img,(ind_d_x,ind_d_y),(thumb_x,thumb_y),(0,255,0),5)
                        pyautogui.press("volumeup")    
                    else:
                        cv2.line(img,(ind_d_x,ind_d_y),(thumb_x,thumb_y),(0,0,255),5)
                        pyautogui.press("volumedown") 
                
                
                # if fingers[1] == 1 and fingers[2] == 0 and fingers[0] == 0 and fingers[3]==0 and fingers[4] == 0:
                #     # print(abs(ind_x - mid_x))
                    
                #     if abs(ind_x - thumb_x3) < 30:
                #         if not dragging:
                #             dragging = True
                #             print("Thumbs Up detected. Start dragging!")
                #             # Simulate mouse down event to start drag
                #             pyautogui.mouseDown()
                #         # print("Touched....")
                #         # # Left Click
                #         # if fingers[1]==1 and fingers[2]==0  and fingers[3]==0 and fingers[0]==0 and fingers[4]==0:
                #         #     mouse.click(button="left")
                #         #     print("Left Click")
                #         #     # l_delay = 1
                #         #     # if not l_clk_thread.is_alive():
                #         #     #     l_clk_thread = threading.Thread(target=l_clk_delay)
                #         #     #     l_clk_thread.start()
                #         #     #     print("Left Click")
                #     else:
                #         if dragging:
                #             dragging = False
                #             print("Thumbs Down detected. Stop dragging!")
                #             # Simulate mouse up event to drop the object
                #             pyautogui.mouseUp()
                #         print("Not Touched...")
                    
                    
                #     if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and dragging:
                #         # Get the wrist position to follow the movement
                #         # wrist = landmarks.landmark[mp_hands.HandLandmark.WRIST]
                #         # x, y = int(wrist.x * frame.shape[1]), int(wrist.y * frame.shape[0])

                #         # # Map wrist coordinates to screen coordinates
                #         # screen_x = min(screen_width, max(0, x * screen_width / frame.shape[1]))
                #         # screen_y = min(screen_height, max(0, y * screen_height / frame.shape[0]))

                #         conv_x = int(np.interp(ind_x, (frameR+30, cam_w - 70), (0, screen_width)))
                #         conv_y = int(np.interp(ind_y, (60, cam_h - frameR -30), (0, screen_height)))
                #         # Move the mouse to tdetected position                                                                                                                                                                              
                #         pyautogui.moveTo(conv_x, conv_y)
        
                #         #right Click
                #         # if fingers[4] == 1 and fingers[1]==1 and fingers[2]==1  and fingers[3]==0 and r_delay == 0:
                #         #     mouse.click(button = "right")
                #         #     r_delay = 1
                #         #     if not r_clk_thread.is_alive():
                #         #         r_clk_thread = threading.Thread(target=r_clk_delay)
                #         #         r_clk_thread.start()
                #         #         print("Right Clickhe ")
                # else :
                #     pyautogui.mouseUp()
                #     dragging = False        

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












'''

import cv2
import mediapipe as mp
# import maths
import pyautogui

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize OpenCV to capture video from webcam
cap = cv2.VideoCapture(0)

# Initialize dragging state
dragging = False

# Set the screen size (optional, for tracking the hand's position on screen)
screen_width, screen_height = pyautogui.size()

def is_thumbs_up(hand_landmarks):
    # Get coordinates for thumb base (Wrist) and thumb tip
    thumb_base = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    
    # Check if the thumb tip is above the thumb base (Thumbs Up)
    return thumb_tip.y < thumb_base.y

def is_thumbs_down(hand_landmarks):
    # Get coordinates for thumb base (Wrist) and thumb tip
    thumb_base = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_CMC]
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    
    # Check if the thumb tip is below the thumb base (Thumbs Down)
    return thumb_tip.y > thumb_base.y

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Convert the BGR frame to RGB as MediaPipe requires RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and get the hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Check if it's a Thumbs Up gesture (start dragging)
            if is_thumbs_up(landmarks):
                if not dragging:
                    dragging = True
                    print("Thumbs Up detected. Start dragging!")
                    # Simulate mouse down event to start drag
                    pyautogui.mouseDown()

            # Check if it's a Thumbs Down gesture (stop dragging)
            if is_thumbs_down(landmarks):
                if dragging:
                    dragging = False
                    print("Thumbs Down detected. Stop dragging!")
                    # Simulate mouse up event to drop the object
                    pyautogui.mouseUp()

            if dragging:
                # Get the wrist position to follow the movement
                wrist = landmarks.landmark[mp_hands.HandLandmark.WRIST]
                x, y = int(wrist.x * frame.shape[1]), int(wrist.y * frame.shape[0])

                # Map wrist coordinates to screen coordinates
                screen_x = min(screen_width, max(0, x * screen_width / frame.shape[1]))
                screen_y = min(screen_height, max(0, y * screen_height / frame.shape[0]))

                # Move the mouse to the detected position
                pyautogui.moveTo(screen_x, screen_y)

            # Draw landmarks and connections
            mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    # Show the frame with the hand landmarks
    cv2.imshow("Hand Gesture Drag and Drop", frame)

    # End loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''