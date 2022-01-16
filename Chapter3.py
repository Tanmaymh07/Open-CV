import cv2
import numpy as np

img = cv2.imread("res/imge.jpg")
print(img.shape)

imgResize = cv2.resize(img,(538,541))
print(imgResize.shape)

imgCropped = img[0:200,200:500]


cv2.imshow("Image",img)
# cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)

