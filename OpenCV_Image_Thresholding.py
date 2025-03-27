import cv2;

img = cv2.imread("image.png")
if img is None:
    print("Image not found")
else:
   print("BGR format [0,0]: ",img[0,0])

gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

rest,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

adaptive=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow("Gray",gray)
cv2.imshow("Threshold",thresh)
cv2.imshow("Adaptive",adaptive)
cv2.waitKey(0)  
cv2.destroyAllWindows()