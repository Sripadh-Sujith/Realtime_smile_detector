import cv2

cap=cv2.VideoCapture(0)
facecascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smilecascade=cv2.CascadeClassifier('haarcascade_smile.xml')

while True:
    success, img=cap.read()
    imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=facecascade.detectMultiScale(imggray,1.1,4)
    

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray = imggray[y:y+h, x:x+w]

        smiles=smilecascade.detectMultiScale(roi_gray,scaleFactor=1.2,minNeighbors=4,minSize=(10,10))

        for (x1,y1,w1,h1) in smiles:
            cv2.putText(img,'Smiling',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            


    cv2.imshow('Webcam',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break