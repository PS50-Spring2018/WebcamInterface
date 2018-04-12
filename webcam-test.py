# Example for how to use the opencv module to campure webcam images

# Import opencv
import time
import cv2
import numpy as np
import ShapeDetector as sd
import CameraOps as co


# Function for displaying continuous video stream
# n: Camera number on computer (usually n=0 for built-in webcam)
# Exit video by clicking into video and pressing ESC key


if __name__=='__main__':

	#Uncomment to stream webcam video
	#stream()

	#Uncomment to take single snap
	#add n in the future to distinguish images from one another, this might be a time 
	s = co.snap(0)
	count=0
	
	r=[]
	b=[]
	g=[]
	#parse image to use in thresholding
	cv2.imwrite("frame%d.jpg" % count, s) 
	img = cv2.imread("frame%d.jpg" % count)
	print(type(img))
	thresh = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY)[1]
	contrs=cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	
	for i in range(s.shape[0]):
		for j in range(s.shape[1]):
			#x
			#y
			#color
			r.append(s[i][j][0])
			b.append(s[i][j][1])
			g.append(s[i][j][2])
			

	r=np.array(r)
	b=np.array(b)
	g=np.array(g)
	mean=[np.mean(r),np.mean(b),np.mean(g)]
	var=[np.var(r),np.var(b),np.var(g)]
	#print(mean)
	#print(var)

	sides=sd.detect(s)
	#print(sides)

