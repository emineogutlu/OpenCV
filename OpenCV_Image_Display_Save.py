import cv2;
image =cv2.imread("image.png");
if image is None:
    print("Image not found");
else:
    cv2.imshow("Image",image);
    # if ord("A") == 65:
    #  cv2.waitKey(ord("A"));,
    cv2.waitKey(0);
    cv2.destroyAllWindows();


cv2.imwrite("image_example.jpg",image);
print("Image saved");