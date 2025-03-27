import cv2;

img = cv2.imread("image.png")
if img is None:
    print("Image not found")
else:
   print("BGR format [0,0]: ",img[0,0])


img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print("RGB format [0,0]: ",img_rgb[0,0])

img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
print("HSV format [0,0]: ",img_hsv[0,0])


cv2.imshow("Orijinal-bgr",img)
cv2.imshow("HSV",img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()