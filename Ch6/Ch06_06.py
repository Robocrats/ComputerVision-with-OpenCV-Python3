import cv2
import os
output='Output_Video.mp4'
images = []
for f in os.listdir():
    if f.endswith('.jpg'):
        images.append(f)
image_path = os.path.join('.', images[0])
img_writer = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter(output, img_writer, 20.0, (1080, 1080))
for image in images:
    image_path = os.path.join('.', image)
    frame = cv2.imread(image_path)
    out.write(frame) 
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break
print("Successful! Converted images into video is saved in {}".format(output))
out.release()
cv2.destroyAllWindows()


