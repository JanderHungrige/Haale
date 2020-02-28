#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:26:09 2020

@author: base
"""
import cv2
import numpy as np
import mtcnn
from mtcnn.mtcnn import MTCNN
import time
# print MTCNN Version
print('mtcnn Versionsnummer: ' + mtcnn.__version__)

detector = MTCNN()
cap = cv2.VideoCapture(0)
p=20 #Radius der Box um das Gesicht
AktuellerWert=[]
Mittelwert=[]

showvideo=True # True oder False. Ohne video ist der face detector natürlich wesentlich schneller


while(True):
    t1=time.time()
    ret, frame = cap.read()
    frame =cv2.flip(frame,1) 
    faces_detected =detector.detect_faces(frame) # Das hier ist das MTCNN Netzwerk
    for i in range(len(faces_detected)):
        (x,y,w,h) = faces_detected[i]['box']
        if showvideo:
            rechteck=cv2.rectangle(frame, (x-p, y-p+2), (x+w+p, y+h+p+2), (0, 255, 0), 2)  
            cv2.imshow('frame', rechteck)   
        
    AktuellerWert.append(len(faces_detected))
    Mittelwert=sum(AktuellerWert)/len(AktuellerWert)
    t2=time.time()
   # print(t2-t1) # Hier könnt Ihr euch auch Zeiten ausgeben lassen
    print('Personen: '+str(Mittelwert))
    if len(AktuellerWert)==25:
        a=[]
        a.append(int(round(Mittelwert)))        
    
    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()