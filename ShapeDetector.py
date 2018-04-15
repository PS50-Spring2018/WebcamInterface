#remember conda install imutils
import cv2
	
def detect(self, c):
	# initialize the shape name and approximate the contour
	contours,hierarchy = cv2.findContours(c, 1, 2)
	
	for i in range(hierarchy):

		print(len(contours[i]))
	


	
	return contours

def circle(cnt): 
    
	cnt = contours[0]

	(x,y),radius = cv2.minEnclosingCircle(cnt)

	center = (int(x),int(y))

	radius = int(radius)

	cv2.circle(img,center,radius,(0,255,0),2)

	return center, radius 
