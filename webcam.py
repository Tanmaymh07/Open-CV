import cv2, time

cap=cv2.VideoCapture(0)
address= "http://192.168.0.101:8080/video"
#cap.read(address)

cap.set(3,640)  #setting width of video
cap.set(4,480)  #height of video 
cap.set(10,100) 
while True:
    sucess, img = cap.read(address)
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


# cap = cv2.VideoCapture(1)
# cap.set(3,640)  #setting width of video
# cap.set(4,480)  #height of video 
# cap.set(10,100) #brightness of video