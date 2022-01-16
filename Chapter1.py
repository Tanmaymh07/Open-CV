import cv2
print("Package Imported")
#reading image 
# #img = cv2.imread("res/imge.jpg")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# reading video
cap = cv2.VideoCapture("res/mrrobot.mp4")

while True:
    sucess, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

# reading video from webcam

cap = cv2.VideoCapture(1)
cap.set(3,640)  #setting width of video
cap.set(4,480)  #height of video 
cap.set(10,100) #brightness of video
 

# while True:
#     sucess, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
