import cv2
import numpy as np
	
def detect(self, initial_img):
	# initialize the shape name and approximate the contour
	
	gray = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
	#print(gray)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	#print(blur)
	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)[1]

	_, cont,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	
	center=[]
	radii=[]

	for line in cont:

		temp=circle(line)
		
		center.append(temp[0])
		
		radii.append(temp[1])
	
	radii=np.array(radii)
	
	ind=np.argmax(radii)

	return center[ind],radii[ind]

def circle(cnt):   

	(x,y),radius = cv2.minEnclosingCircle(cnt)

	center = (int(x),int(y))

	radius = int(radius)

	return center, radius 
