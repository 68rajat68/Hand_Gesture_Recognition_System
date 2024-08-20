import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector  # For hand tracking
from cvzone.ClassificationModule import Classifier
import math
# from TrainModel import load_data

cap=cv2.VideoCapture(0)

detector=HandDetector(maxHands=1)

classifier = Classifier("Model/keras_model_05.h5","Model/labels_05.txt")
# model = load_data('my_model.h5')

offset = 20      # it is used to make some offset in the croped image
imgSize = 300

folder = "Data/"

priviousAlphabet = ""
priviousAlphabet2 = ""
currentAlphabet = ""
currentWord = ""
nextAlphabet = False
accuracy = 0.00
threshold =0.98

labels = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

while True:
    success, img =cap.read()
    imgOutput = img.copy()
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
            # prediction, index =classifier.getPrediction(imgWhite,draw=False)
            # currentAlphabet = labels[index]
        else :
            k = imgSize/w
            hCal= math.ceil(h*k)
            imgResize = cv2.resize(imgCrop,(imgSize,hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize-hCal)/2)
            imgWhite[hGap:(hGap+hCal),:] = imgResize
            # prediction, index =classifier.getPrediction(imgWhite,draw=False)
            # currentAlphabet = labels[index]
            # accuracy = prediction[np.argmax[prediction]]
            
        prediction, index =classifier.getPrediction(imgWhite,draw=False)
        # prediction = model.predict(np.array([imgWhite]))[0]
        # index = np.argmax(prediction)
        
        if(index != 77):
            currentAlphabet = labels[index]
            nextAlphabet=False
        elif(priviousAlphabet2 != labels[index]):
            nextAlphabet = True
            priviousAlphabet=""
            priviousAlphabet2 = labels[index]
            
        accuracy = prediction[np.argmax(prediction)]
        
        if(((priviousAlphabet=="") or (priviousAlphabet!=currentAlphabet))  and accuracy > threshold and nextAlphabet==False):
            currentWord += currentAlphabet
            priviousAlphabet = currentAlphabet
            if(nextAlphabet == False):
                priviousAlphabet2 = currentAlphabet
            # nextAlphabet =False
        
        # if currentAlphabet: 
        #     currentWord += currentAlphabet
        #     priviousAlphabet = currentAlphabet
        
        cv2.imshow("ImageCrop",imgCrop)
        cv2.imshow("ImageWhite",imgWhite)
        
        cv2.rectangle(imgOutput,(x-offset,y-offset-50),(x+145,y-offset-10),(35,255,50),cv2.FILLED)                                   # Backgroud for displed text
        cv2.rectangle(imgOutput,(x-offset-5,y-offset-55),(x+150,y-offset-5),(0,0,0),2)                                               # Border for upper box
        if(index==77):
            cv2.putText(imgOutput,labels[index],(x-offset+5,y-40),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)                       # Alphabet printing
            cv2.putText(imgOutput,"-"+str(round((accuracy*100),2)) + "%",(x+50,y-40),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)    # Accuracy printing
        else:
            cv2.putText(imgOutput,labels[index],(x-offset+5,y-40),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(0,0,0),2)                      # Alphabet printing
            cv2.putText(imgOutput,"-"+str(round((accuracy*100),2)) + "%",(x+10,y-40),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),2)    # Accuracy printing
        cv2.rectangle(imgOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(34,255,50),2)                                          # Rectangle on hand
        cv2.rectangle(imgOutput,(x-offset-5,y-offset-5),(x+w+offset+5,y+h+offset+5),(0,0,0),2)                                      # Rectangle Border for hand
    cv2.rectangle(imgOutput,(0,460),(640,480),(34,255,50),cv2.FILLED)                                                               # Backgroud for displed Word
    # cv2.putText(imgOutput,"Word: " + currentWord,(10,475),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),2)                                       # Word Printing
         
    cv2.imshow("Image",imgOutput)
    cv2.waitKey(1)
