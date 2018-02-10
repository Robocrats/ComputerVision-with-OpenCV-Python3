import cv2
import numpy as np
import os
def find_repeat():
    for file_type in ['stamp']:
        for img in os.listdir(file_type):
            for repeat_img in os.listdir('duplicate'):
                try:
                    current_image_path =str(file_type)+'/'+str(img)
                    Duplicate= cv2.imread('duplicate/'+str(repeat_img))
                    question=cv2.imread(current_image_path)
                    if Duplicate.shape==question.shape and not(np.bitwise_xor(Duplicate,question).any()):
                           print('Repetitive!')
                           print(current_image_path)
                           os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
find_repeat()

