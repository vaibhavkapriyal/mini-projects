import cv2




path = r'D:\mini_project\semester 4\test.jpg'
image = cv2.imread(path)
cv2.imshow("original image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
