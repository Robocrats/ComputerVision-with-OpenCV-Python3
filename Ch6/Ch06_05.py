import numpy as np
import cv2
canvas = np.ones([480,640,3],'uint8')*255
radius = 3
color = (0,255,0)
pressed = False
def click(event, x, y, flags, param):
	global canvas, pressed
	if event == cv2.EVENT_LBUTTONDOWN:
		pressed = True
		cv2.circle(canvas,(x,y),radius,color,-1)
	elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
		cv2.circle(canvas,(x,y),radius,color,-1)
	elif event == cv2.EVENT_LBUTTONUP:
		pressed = False
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", click)
while True:
    cv2.imshow("Paint",canvas)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    elif ch & 0xFF == ord('b'):
        color = (255,0,0)
    elif ch & 0xFF == ord('g'):
        color = (0,255,0)
    elif ch & 0xFF == ord('r'):
        color = (0,0,255)
cv2.destroyAllWindows()

