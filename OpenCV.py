#import matplotlib.pyplot as plt
import cv2
img=cv2.imread("/home/divyakshi/Desktop/images/download.jpeg")
#cimage=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("t",img)
#plt.imshow(cimage)
#plt.show()
cap= cv2.VideoCapture(0)
face= cv2.CascadeClassifier('/home/divyakshi/Desktop/Face.xml')
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale2(gray, 1.3, 5)
    if ret is False:
        continue
    #cv2.imshow("Frame", frame)
    for (x,y,z,w) in faces:
        cv2.rectangle(frame,(x,y),(x+z,y+w), (255, 0, 0), 2)
    #cv2.imshow("Gray", gray)
    pressed=cv2.waitKey(1) & 0xFF
    if pressed == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()