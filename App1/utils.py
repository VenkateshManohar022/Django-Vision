from django.conf import settings
import cv2
import os

def selectionChoices(image,choice):
    if choice == 'GRAY':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif choice == 'HSV':
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    elif choice == 'BLUR':
        return cv2.blur(image, (15, 15))
    elif choice == 'EDGE':
        return cv2.Canny(image,50,120)
    elif choice == 'FACE':
        data = ""
        face_classifier = cv2.CascadeClassifier(os.path.join(settings.STATICFILES_DIRS[0],'Haarcascades/haarcascade_frontalface_default.xml'))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        for (x,y,w,h) in faces:
            data = cv2.rectangle(image, (x,y), (x+w,y+h), (127,0,255), 2)
        return data
