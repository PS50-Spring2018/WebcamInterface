import cv2
import numpy as np
	
def detect(self, s):
	# initialize the shape name and approximate the contour
	#contours,hierarchy = cv2.findContours(c, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#print(img)
	gray = cv2.cvtColor(s, cv2.COLOR_BGR2GRAY)
	#print(gray)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	#print(blur)
	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
	#ask tim about the module not allowing thresh to pass
	
	_, cont,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	center=[]
	radii=[]

	for line in cont:

		temp=circle(s,line)
		
		center.append(temp[0])
		
		radii.append(temp[1])
	
	radii=np.array(radii)
	
	ind=np.argmax(radii)
	#for i in range(hierarchy):

	#	print(circle(contours[i]))
	

	return center[ind],radii[ind]

def circle(img,cnt): 
    

	(x,y),radius = cv2.minEnclosingCircle(cnt)

	center = (int(x),int(y))

	radius = int(radius)

	cv2.circle(img,center,radius,(0,255,0),2)

	return center, radius 
