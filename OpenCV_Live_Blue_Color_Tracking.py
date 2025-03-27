import cv2;
import numpy as np;

cap=cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot open camera")
        break

    hsv_image =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,150,50])
    upper_blue = np.array([140,255,255])

    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    result=cv2.bitwise_and(frame, frame, mask=mask)

    counters, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  

    for contour in counters:
       if cv2.contourArea(contour) > 500:
          x,y,w,h = cv2.boundingRect(contour)
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Blur Color Detection",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()