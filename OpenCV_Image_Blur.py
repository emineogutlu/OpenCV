import cv2;

img = cv2.imread("image.png")
if img is None:
    print("Image not found")
else:
   
   gaussblur=cv2.GaussianBlur(img,(5,5),0)
   mediunblur=cv2.medianBlur(img,5)

   cv2.imshow("Orijinal",img)
   cv2.imshow("Gauss",gaussblur)
   cv2.imshow("Median",mediunblur)
   cv2.waitKey(0)
   cv2.destroyAllWindows()