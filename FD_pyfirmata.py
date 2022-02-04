import pyfirmata as fir
from pyfirmata import Arduino, SERVO
import cv2
from cvzone.FaceDetectionModule import FaceDetector
from time import sleep

cap = cv2.VideoCapture(0)
 
detector = FaceDetector(minDetectionCon=0.6)

a = Arduino('COM5')
a.digital[13].mode = fir.OUTPUT #LED
a.digital[11].mode = fir.OUTPUT #Buzzer
a.digital[9].mode = SERVO #Servo


while(cap.isOpened()):
    ret, img = cap.read()
    if ret==True:
           
            img, bboxes = detector.findFaces(img)

            if bboxes:
                #If face detected ,LED ON ,Buzzer ON and rotate servo to open the door
                a.digital[13].write(1)

                a.digital[11].write(1)

                for pos in (0,50):
                    a.digital[9].write(pos)
                    sleep(0.015) #15ms delay

                
        
            else:
                a.digital[13].write(0)
                a.digital[11].write(0)
                for i in range(50,0,-1):
                    a.digital[9].write(i)
                    sleep(0.015) #15ms delay to adjust
            cv2.imshow("Image",img)
            if cv2.waitKey(1) & 0xFF == ord('q'): #Press Button "Q/q" to exit the window
                break
            
    else:
        break
cap.release()
cv2.destroyAllWindows()
               
            