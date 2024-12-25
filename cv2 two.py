#this is the Copy of the original with modifications so it actually work 
import cv2
import mediapipe as mp 
from Assistance_module import HandDetector
from pyfirmata2 import Arduino, util

#open the port to the first Arduino
Arduino_port = Arduino('/dev/cu.usbmodem11401')

key = util.Iterator(Arduino_port)
key.start()

#open the port to the second Arduino
Arduino_port2 = Arduino('/dev/cu.usbmodem11201')

key = util.Iterator(Arduino_port2)
key.start()

#determining what is what for the fingers that are going to be raised
thumb = Arduino_port.get_pin('d:13:o')
index = Arduino_port.get_pin('d:12:o')
middle = Arduino_port.get_pin('d:11:o')
ring = Arduino_port.get_pin('d:10:o')
pinky = Arduino_port.get_pin('d:9:o')

#determining what is what for the middle function
index_middle = Arduino_port2.get_pin('d:9:o')
middle_middle = Arduino_port2.get_pin('d:10:o')
ring_middle = Arduino_port2.get_pin('d:11:o')
pinky_middle = Arduino_port2.get_pin('d:12:o')


handdetector = HandDetector()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    img = handdetector.find_hands(img)
    land_mark_list = handdetector.find_positions(img)
    #print(land_mark_list)

    fingers_up = handdetector.fingers_ups()
    print("The fingers that are up are:", fingers_up,)


    fingers_middles = handdetector.fingers_middle()
    print("The fingers that are middled are:", fingers_middles)
  
    
    cv2.imshow('hand detection', img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        thumb.write(0)
        index.write(0) 
        middle.write(0) 
        ring.write(0) 
        pinky.write(0)

        index_middle.write(0)
        middle_middle.write(0)
        ring_middle.write(0)
        pinky_middle.write(0)


        break

    