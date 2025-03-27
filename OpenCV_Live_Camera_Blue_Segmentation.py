import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        lower_blue = np.array([100, 0, 0])
        upper_blue = np.array([255, 100, 100])

        mask = cv2.inRange(frame, lower_blue, upper_blue)

        blue_segment = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Live Camera", blue_segment)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
