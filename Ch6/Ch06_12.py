import cv2
import math
refPt = [ ]
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cv2.circle(img,(x,y),5,(255,0,0),-1)
        print(x,y)
img = cv2.imread("shape.jpg")
(sizex,sizey,z)=img.shape;
cv2.namedWindow('Calculate Angle')
cv2.setMouseCallback('Calculate Angle',draw_circle)
while(1):
    cv2.imshow('Calculate Angle',img)
    if len(refPt) == 3:
        for i in range(1,3,1):
            cv2.putText(img,str(i+1),refPt[i], 1, 3,(255,0,0))
            cv2.line(img,refPt[i-1],refPt[i],(255,0,0),3)
            (x0,y0)=refPt[0];
            (x1,y1)=refPt[1];
            (x2,y2)=refPt[2];
            a = (x1-x0)**2 + (y1-y0)**2
            b = (x1-x2)**2 + (y1-y2)**2
            c = (x2-x0)**2 + (y2-y0)**2
            angle= math.acos((a+b-c)/math.sqrt(4*a*b))*180/3.14
            ang=round(angle);
            cv2.rectangle(img,(sizey-100,sizex-50),(sizey,sizex),(0,255,255),-1)
            cv2.putText(img,str(ang),(sizey-95,sizex-20),5,1,(0,0,0))
            cv2.putText(img,str("Deg"),(sizey-50,sizex-20),5,1,(0,0,0))   
        del refPt[:]
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
