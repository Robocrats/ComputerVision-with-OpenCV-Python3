import cv2
import os
facePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(facePath)
def get_images():
    if not os.path.exists('database'):
        os.makedirs('database')
    pic_num = len(os.listdir('database/'))
    for file_type in ['stamp']:
        for img in os.listdir(file_type):
                try:
                    image_path =str(file_type)+'/'+str(img)
                    img=cv2.imread(image_path)
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = faceCascade.detectMultiScale(gray,scaleFactor= 1.05,
                            minNeighbors=8,minSize=(55, 55),flags=cv2.CASCADE_SCALE_IMAGE)
                    for (x, y, w, h) in faces:
                        resized_image = img[y:y+h, x:x+w]
                        cv2.imwrite("database/"+str(pic_num)+'.jpg',resized_image)
                        pic_num +=1
                        print('Sucessful')
                        print(image_path)
                except Exception as e:
                    print(str(e))
get_images()
