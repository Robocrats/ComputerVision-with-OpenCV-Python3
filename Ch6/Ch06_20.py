import numpy as np
import cv2
def roi(img, vertices):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        channel_count = img.shape[2] 
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
lower_yellow = np.array([20, 100, 100], dtype = "uint8")
upper_yellow = np.array([30, 255, 255], dtype="uint8")
cap = cv2.VideoCapture('3.mp4')
while(True):
    ret, frame = cap.read()
    imshape = frame.shape
    line_img = np.zeros((imshape[0],imshape[1],3), dtype=np.uint8)
    lower_left = [imshape[1]/9,imshape[0]]
    lower_right = [imshape[1]-imshape[1]/9,imshape[0]]
    top_left = [imshape[1]/2-imshape[1]/8,imshape[0]/2+imshape[0]/10]
    top_right = [imshape[1]/2+imshape[1]/8,imshape[0]/2+imshape[0]/10]
    vertices = [np.array([lower_left,top_left,top_right,lower_right],dtype=np.int32)]
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_white = cv2.inRange(gray, 200, 255)
    mask_yw = cv2.bitwise_or(mask_white, mask_yellow)
    mask_yw_image = cv2.bitwise_and(gray, mask_yw)
    kernel_size = 2
    gauss_gray = cv2.GaussianBlur(mask_yw_image,(5,5),kernel_size)
    edges = cv2.Canny(gauss_gray, 50, 150)
    roi_image = roi(edges, vertices)
    lines = cv2.HoughLinesP(roi_image,2, np.pi/180, 20, np.array([]), minLineLength=50, maxLineGap=200)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2),(0,0,255),5)
            lines=lines+1
            final = cv2.addWeighted(frame, 0.8, line_img, 1,0)
    cv2.imshow('frame',final)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()