import numpy as np

import cv2 

# load a color image
img = cv2.imread('berserk1.png', 1)
# Draw a diagonal blue line with a thickness of 5px
cv2.line(img,(0,0),(300,300), (255,0,0), 15)
# Draw a green rectangle 
cv2.rectangle(img,(500,0),(900,222),(0,255,0),3)
# Draw a circle inside rectangle
cv2.circle(img,(800,80), 63, (0,0,255), -1)
# Draw a half ellpise
cv2.ellipse(img,(333,333),(100,50),0,0,180,255,-1)

# Draw a polygon
pts = np.array([[400,55],[300,100],[300,50],[400,60]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(255,0,0))

# Write my name at the bottom of the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Callum McLaughlin',(100,1000), font, 3,(255,255,255),2,cv2.LINE_AA)

# Display Image
cv2.imshow('image', img)
cv2.resizeWindow('image', 1024, 1024)

k = cv2.waitKey(0)
if k == 27: # wait for esc key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
          cv2.imwrite('berserkgray.png', img)
cv2.destroyAllWindows()

