import cv2

img = cv2.imread("image.png")
if img is None:
    print("Image not found")

else:
    print("Original size (Y, X):", img.shape[:2])

    half = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    print("Half size (Y, X):", half.shape[:2])

    enlarged = cv2.resize(half, img.shape[1::-1])
    print("Enlarged size (Y, X):", enlarged.shape[:2])

    cv2.imshow("Original", img)
    cv2.imshow("Half size", half)
    cv2.imshow("Enlarged", enlarged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()