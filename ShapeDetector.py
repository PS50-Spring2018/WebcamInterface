import cv2
import numpy as np
	
def detect(self, initial_img):
	# initialize the shape name and approximate the contour
	#contours,hierarchy = cv2.findContours(c, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	#print(img)

	#derived from https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/

	gray = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
	#print(gray)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	#print(blur)
	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
	#ask tim about the allowing thresh to pass

	#cv2.namedWindow("test")

	cv2.imshow("test",thresh)
	#cv2.waitKey(0)
	#find contours isn't working
	_, cont,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	#print(len(cont))

	#cv2.imshow("test",cv2.drawContours(thresh, cont, -1, (0,255,0), 8))

	center=[]
	radii=[]

	for line in cont:

		line = cv2.approxPolyDP(line, 0.01 * cv2.arcLength(line, True), True)

		temp=circle(line)
		
		center.append(temp[0])
		
		radii.append(temp[1])
	
	radii=np.array(radii)
	
	ind=np.argmax(radii)

	print(center[ind],radii[ind])

	for i in range(len(center)):
		cv2.imshow("test",cv2.circle(initial_img,center[i],radii[i],(0,255,0),2))

	#cv2.waitKey(0)

	return center[ind],radii[ind]

def circle(cnt): 
    

	(x,y),radius = cv2.minEnclosingCircle(cnt)

	center = (int(x),int(y))

	radius = int(radius)

	return center, radius 


def circledetect(x,y,center,radius):

	vect=np.array([(x-center[0]),(y-center[0])])
	
	if np.linalg.norm(vect)<radius: 
	
		return True
	
	else:
	
		return False 
