import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector  # For hand tracking 
import math

cap=cv2.VideoCapture(0)

detector=HandDetector(maxHands=1)
offset = 20      # it is used to make some offset in the croped image
imgSize = 300

folder = "Data/"
count = 0

while True:
    success, img =cap.read()
    hands,img = detector.findHands(img)  # For detecting hand
    if hands:
        hand =hands[0]
        x,y,w,h = hand['bbox']
        # we multiply it by 255 to make color white.
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255        # np.uint8 is used to give it datatype as unsigned int of 8 bits (i.e. values from 0 to 255)
        
        imgCrop = img[y-offset:y+h+offset ,x-offset:x+w+offset]
        
        
        imgCropShape = imgCrop.shape
        if(hand!=None):
        # we have to put this croped image to the center of the white image 
            aspectRatio = h/w
            
            if aspectRatio>1:
                k = imgSize/h
                wCal = math.ceil(k*w)
                imgResize = cv2.resize(imgCrop,(wCal,imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal)/2)
                imgWhite[:,wGap:(wGap+wCal)] = imgResize
            
            else :
                k = imgSize/w
                hCal= math.ceil(h*k)
                imgResize = cv2.resize(imgCrop,(imgSize,hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize-hCal)/2)
                imgWhite[hGap:(hGap+hCal),:] = imgResize
        
            
        # To show images on Screen
         
        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite",imgWhite)
    
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    
    if key == ord('a'):
        cv2.imwrite(f'{folder}/A/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('b'):
        cv2.imwrite(f'{folder}/B/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('c'):
        cv2.imwrite(f'{folder}/C/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('d'):
        cv2.imwrite(f'{folder}/D/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    # if key == ord('q'):
    #     cv2.imwrite(f'{folder}/newAlphabet/Image_{count}.jpg',imgWhite)
    #     count += 1
    #     print(count)
    # if key == ord('t'):
    #     cv2.imwrite(f'{folder}/Space/Image_{count}.jpg',imgWhite)
    #     count += 1
    #     print(count)
    if key == ord('e'):
        cv2.imwrite(f'{folder}/E/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('f'):
        cv2.imwrite(f'{folder}/F/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('g'):
        cv2.imwrite(f'{folder}/G/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('h'):
        cv2.imwrite(f'{folder}/H/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('i'):
        cv2.imwrite(f'{folder}/I/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('j'):
        cv2.imwrite(f'{folder}/J/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('k'):
        cv2.imwrite(f'{folder}/K/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('l'):
        cv2.imwrite(f'{folder}/L/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('m'):
        cv2.imwrite(f'{folder}/M/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('n'):
        cv2.imwrite(f'{folder}/N/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('o'):
        cv2.imwrite(f'{folder}/O/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('p'):
        cv2.imwrite(f'{folder}/P/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('q'):
        cv2.imwrite(f'{folder}/Q/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('r'):
        cv2.imwrite(f'{folder}/R/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('s'):
        cv2.imwrite(f'{folder}/S/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('t'):
        cv2.imwrite(f'{folder}/T/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('u'):
        cv2.imwrite(f'{folder}/U/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('v'):
        cv2.imwrite(f'{folder}/V/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('w'):
        cv2.imwrite(f'{folder}/W/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('x'):
        cv2.imwrite(f'{folder}/X/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('y'):
        cv2.imwrite(f'{folder}/Y/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('z'):
        cv2.imwrite(f'{folder}/Z/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)

# import cv2
# import numpy as np
# from cvzone.HandTrackingModule import HandDetector  # For hand tracking 
# import math

# cap = cv2.VideoCapture(0)
# detector = HandDetector(maxHands=2)  # Set maxHands to 2 for detecting both hands
# offset = 20
# imgSize = 600
# folder = "Data/"
# count = 0

# # Use a list to store information for each hand
# hand_data = [{}, {}]

# while True:
#     success, img = cap.read()
#     hands, img = detector.findHands(img)  # For detecting hands
#     if hands:
#         for i, hand in enumerate(hands):
#             x, y, w, h = hand['bbox']
#             imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

#             imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

#             aspectRatio = h / w

#             if aspectRatio > 1:
#                 k = imgSize / h
#                 wCal = math.ceil(k * w)
#                 imgResize = cv2.resize(imgCrop, (wCal, imgSize))
#                 wGap = math.ceil((imgSize - wCal) / 2)
#                 imgWhite[:, wGap:(wGap + wCal)] = imgResize
#             else:
#                 k = imgSize / w
#                 hCal = math.ceil(h * k)
#                 imgResize = cv2.resize(imgCrop, (imgSize, hCal))
#                 hGap = math.ceil((imgSize - hCal) / 2)
#                 imgWhite[hGap:(hGap + hCal), :] = imgResize

#             # To show images on Screen
#             # cv2.imshow(f"ImageCrop Hand {i+1}", imgCrop)
#             cv2.imshow(f"ImageWhite Hand {i+1}", imgWhite)

#             # Store data for each hand
#             hand_data[i] = {'x': x, 'y': y, 'w': w, 'h': h, 'imgWhite': imgWhite}

#     cv2.imshow("Image", img)
#     key = cv2.waitKey(1)

#     # Store data for each hand when the corresponding key is pressed
#     for i, hand_key in enumerate(['a', 'b']):
#         if key == ord(hand_key):
#             if hand_data[i]:
#                 x, y, w, h = hand_data[i]['x'], hand_data[i]['y'], hand_data[i]['w'], hand_data[i]['h']
#                 imgWhite = hand_data[i]['imgWhite']
#                 cv2.imwrite(f'{folder}/{hand_key.upper()}/Image_{count}.jpg', imgWhite)
#                 count += 1
#                 print(count)

#     if key == 27:  # 27 is the ASCII code for the ESC key, press ESC to exit the loop
#         break

"""

import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector  # For hand tracking 
import math


cap=cv2.VideoCapture(0)

detector=HandDetector(maxHands=2)
offset = 20      # it is used to make some offset in the croped image
imgSize = 600

folder = "Data/"
count = 0

while True:
    success, img =cap.read()
    hands,img = detector.findHands(img)  # For detecting hand
    if hands:
        hand =hands[0]
        x,y,w,h = hand['bbox']
        # we multiply it by 255 to make color white.
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255        # np.uint8 is used to give it datatype as unsigned int of 8 bits (i.e. values from 0 to 255)
        
        imgCrop = img[y-offset:y+h+offset ,x-offset:x+w+offset]
        
        
        imgCropShape = imgCrop.shape
        
        # we have to put this croped image to the center of the white image 
        aspectRatio = h/w
        
        if aspectRatio>1:
            k = imgSize/h
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop,(wCal,imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal)/2)
            imgWhite[:,wGap:(wGap+wCal)] = imgResize
        
        else :
            k = imgSize/w
            hCal= math.ceil(h*k)
            imgResize = cv2.resize(imgCrop,(imgSize,hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:(hGap+hCal),:] = imgResize
        
            
        # To show images on Screen
         
        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite",imgWhite)
    
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    
    if key == ord('a'):
        cv2.imwrite(f'{folder}/A/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('b'):
        cv2.imwrite(f'{folder}/B/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('c'):
        cv2.imwrite(f'{folder}/C/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
    if key == ord('d'):
        cv2.imwrite(f'{folder}/D/Image_{count}.jpg',imgWhite)
        count += 1
        print(count)
        
"""

# import cv2
# import numpy as np
# from cvzone.HandTrackingModule import HandDetector  # For hand tracking 
# import math

# cap = cv2.VideoCapture(0)
# detector = HandDetector(maxHands=2)  # Set maxHands to 2 for detecting both hands
# offset = 20
# imgSize = 300
# folder = "Data/"
# count = 0
# hand_data = [{}, {}]

# while True:
#     success, img = cap.read()
#     hands, img = detector.findHands(img)  # For detecting hands

#     # Create a blank image to store both hands
#     imgWhite = np.ones((imgSize, 2 * imgSize,3), np.uint8) * 255

#     if hands:
#         for i, hand in enumerate(hands):
#             x, y, w, h = hand['bbox']
            
#             # hand_region_width = min(imgSize, w + 2 * offset)
#             # hand_region = imgWhite[y - offset:y + h + offset, i * imgSize + (imgSize - hand_region_width) // 2:i * imgSize + (imgSize - hand_region_width) // 2 + hand_region_width]
#             # Determine the region for each hand in the combined image
#             # hand_region = imgWhite[y - offset:y + h + offset, i * imgSize + x - offset:i * imgSize + x + w + offset]

#             imgCrop = img[y-offset:y+h+offset ,x-offset:x+w+offset]
            
            
#             # aspect_ratio = h / w
#             # if aspect_ratio > 1:
#             #     k = imgSize / h
#             #     w_cal = math.ceil(k * w)
#             #     # img_resize = cv2.resize(imgCrop[y:y + h, x:x + w], (w_cal, imgSize))
#             #     img_resize = cv2.resize(imgCrop,(w_cal,imgSize))
#             #     w_gap = math.ceil((imgWhite.shape[1] - w_cal) / 2)
#             #     imgWhite[:,w_gap:w_gap + w_cal]=img_resize
#             #     # hand_region[:min(img_resize.shape[0], hand_region.shape[0]), :min(img_resize.shape[1], hand_region.shape[1])] = img_resize[:min(img_resize.shape[0], hand_region.shape[0]), :min(img_resize.shape[1], hand_region.shape[1])]
#             # else:
#             #     k = imgSize / w
#             #     h_cal = math.ceil(h * k)
#             #     # img_resize = cv2.resize(imgCrop[y:y + h, x:x + w], (2*imgSize, h_cal))
#             #     img_resize = cv2.resize(imgCrop,(2*imgSize,h_cal))
#             #     h_gap = math.ceil((imgWhite.shape[0] - h_cal) / 2)
#             #     imgWhite[h_gap:h_gap + h_cal, :] = img_resize
#             #     # hand_region[:min(img_resize.shape[0], hand_region.shape[0]), :min(img_resize.shape[1], hand_region.shape[1])] = img_resize[:min(img_resize.shape[0], hand_region.shape[0]), :min(img_resize.shape[1], hand_region.shape[1])]

#             # if aspect_ratio > 1:
#             #     k = imgSize / h
#             #     w_cal = math.ceil(k * w)
#             #     img_resize = cv2.resize(img[y:y + h, x:x + w], (w_cal, imgSize))
#             #     w_gap = math.ceil((imgSize - w_cal) / 2)
#             #     hand_region[:, w_gap:w_gap + w_cal] = img_resize
#             # else:
#             #     k = imgSize / w
#             #     h_cal = math.ceil(h * k)
#             #     img_resize = cv2.resize(img[y:y + h, x:x + w], (imgSize, h_cal))
#             #     h_gap = math.ceil((imgSize - h_cal) / 2)
#             #     hand_region[h_gap:h_gap + h_cal, :] = img_resize
            
#             # hand_data[i] = {'x': x, 'y': y, 'w': w, 'h': h, 'imgCrop': imgCrop}
#             hand_data.append({'x': x, 'y': y, 'w': w, 'h': h, 'imgCrop': imgCrop})
#             print(hand_data)
#             # To show images on Screen
#             cv2.imshow(f"ImageCrop Hand {i+1}", img[y - offset:y + h + offset, x - offset:x + w + offset])
            
#             # if hand_region.shape[0] > 0 and hand_region.shape[1] > 0:
#             #     cv2.imshow(f"ImageWhite Hand {i+1}", hand_region)
#             # else:
#             #     print("Invalid hand region dimensions. Skipping display.")
#             # cv2.imshow(f"ImageCrop Hand {i+1}", img[y - offset:y + h + offset, x - offset:x + w + offset])
#             # cv2.imshow(f"ImageWhite Hand {i+1}", hand_region)
           
#         if len(hand_data) >= 2: 
#             hand1_data = hand_data[0]
#             x1 = hand1_data.get('x',None)
#             y1 = hand1_data.get('y',None)
#             w1 = hand1_data.get('w',None)
#             h1 = hand1_data.get('h',None)
#             imgCrop1 = hand1_data.get('imgCrop',None)
            
#             hand2_data = hand_data[1]
#             x2 = hand2_data.get('x',None)
#             y2 = hand2_data.get('y',None)
#             w2 = hand2_data.get('w',None)
#             h2 = hand2_data.get('h',None)
#             imgCrop2 = hand2_data.get('imgCrop',None)
        
#             if(h1 is not None and h2 is not None):
#                 height = max(h1, h2)
                
                
#                 # combined_img = np.ones((height, 2 * img1.shape[1], 3), dtype=np.uint8) * 255
#                 # combined_width = img1.shape[1] + img2.shape[1]
#                 if x1 < x2:
#                     print("Hello")
#                     img1 = cv2.resize(imgCrop1, (int(w1 * height / h1), height))
#                     img2 = cv2.resize(imgCrop2, (int(w2 * height / h2), height))
#                     combined_width = img1.shape[1] + img2.shape[1]
#                     combined_img = np.ones((height, combined_width, 3), dtype=np.uint8) * 255
#                     # Paste img1 on the left side
#                     combined_img[:, :img1.shape[1]] = img1

#                     # Paste img2 on the right side
#                     # combined_img[:, img1.shape[1]:img1.shape[1] + img2.shape[1]] = img2
#                     combined_img[:, img1.shape[1]:img1.shape[1] + img2.shape[1]] = img2
#                     # combined_img[:, img1.shape[1]:] = img2[:, :combined_width - img1.shape[1]]
#                 else:
#                     print("Hell...........o")
#                     img1 = cv2.resize(imgCrop2, (int(w1 * height / h1), height))
#                     img2 = cv2.resize(imgCrop1, (int(w2 * height / h2), height))
#                     combined_width = img1.shape[1] + img2.shape[1]
#                     combined_img = np.ones((height, combined_width, 3), dtype=np.uint8) * 255
#                     # Paste img1 on the left side
#                     combined_img[:, :img1.shape[1]] = img1

#                     # Paste img2 on the right side
#                     # combined_img[:, img1.shape[1]:img1.shape[1] + img2.shape[1]] = img2
#                     combined_img[:, img1.shape[1]:img1.shape[1] + img2.shape[1]] = img2
#                     # combined_img[:, img1.shape[1]:] = img2[:, :combined_width - img1.shape[1]]
                    
#                 cv2.imshow('Combined Image', combined_img)

        
#     # cv2.imshow("Combined Image", combined_img)
#     cv2.imshow("Image", img)
    
#     key = cv2.waitKey(1)

#     # Store data for combined image when a specific key is pressed
#     if key == ord('c'):
#         cv2.imwrite(f'{folder}/Combined/Image_{count}.jpg', imgWhite)
#         count += 1
#         print(count)

#     if key == 27:  # 27 is the ASCII code for the ESC key, press ESC to exit the loop
#         break












# import cv2
# import numpy as np
# from cvzone.HandTrackingModule import HandDetector
# import math

# cap = cv2.VideoCapture(0)

# detector = HandDetector(maxHands=2)  # Increase maxHands to 2 for detecting two hands
# offset = 20
# imgSize = 300
# folder = "Data/"
# count = 0
# hand_data = []

# while True:
#     success, img = cap.read()
#     hands, img = detector.findHands(img)

#     if hands:
#         hand_data.clear()  # Clear previous hand data
#         for i, hand in enumerate(hands):
#             x, y, w, h = hand['bbox']
#             imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
#             hand_data.append({'x': x, 'y': y, 'w': w, 'h': h, 'imgCrop': imgCrop})
#             cv2.imshow(f"ImageCrop Hand {i+1}", imgCrop)

#         if len(hand_data) == 2:
#             hand1_data = hand_data[0]
#             x1, y1, w1, h1, imgCrop1 = hand1_data['x'], hand1_data['y'], hand1_data['w'], hand1_data['h'], hand1_data['imgCrop']

#             hand2_data = hand_data[1]
#             x2, y2, w2, h2, imgCrop2 = hand2_data['x'], hand2_data['y'], hand2_data['w'], hand2_data['h'], hand2_data['imgCrop']

#             # Combine two hands into a single image
#             height = max(h1, h2)
#             img1 = cv2.resize(imgCrop1, (int(w1 * height / h1), height))
#             img2 = cv2.resize(imgCrop2, (int(w2 * height / h2), height))

#             # Determine the order of hands and paste them accordingly
#             if x1 < x2:
#                 combined_width = img1.shape[1] + img2.shape[1]
#                 combined_img = np.ones((height, combined_width, 3), dtype=np.uint8) * 255
#                 combined_img[:, :img1.shape[1]] = img1
#                 combined_img[:, img1.shape[1]:] = img2
#             else:
#                 combined_width = img1.shape[1] + img2.shape[1]
#                 combined_img = np.ones((height, combined_width, 3), dtype=np.uint8) * 255
#                 combined_img[:, :img2.shape[1]] = img2
#                 combined_img[:, img2.shape[1]:] = img1

#             cv2.imshow('Combined Image', combined_img)

#     cv2.imshow("Image", img)
#     key = cv2.waitKey(1)

#     if key == ord('c'):
#         cv2.imwrite(f'{folder}/Combined/Image_{count}.jpg', combined_img)
#         count += 1
#         print(count)

#     if key == 27:
#         break

























