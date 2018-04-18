# Example for how to use the opencv module to campure webcam images

# Import opencv
import cv2
import numpy as np
import ShapeDetector as sd
import CameraOps as co
from matplotlib import image as im

# Function for displaying continuous video stream
# n: Camera number on computer (usually n=0 for built-in webcam)
# Exit video by clicking into video and pressing ESC key



if __name__=='__main__':

	#Uncomment to take single snap
	#add n in the future to distinguish images from one another, this might be a time 
	
	#change this to 1 to use the webcam
	s = co.snap(0)
	count=0
	
	r1,r2,r3,r4,r5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
	b1,b2,b3,b4,b5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
	g1,g2,g3,g4,g5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])


	
	cv2.imwrite("frame%d.jpg" % count, s)

	np.save("frame%d_np.npy" % count,s)
	
	img = cv2.imread("frame%d.jpg" % count)
	
	cv2.namedWindow("Display")
	
	center, radius=sd.detect(sd, img)
	
	cv2.imshow("Display",cv2.circle(img,center,radius,(0,255,0),2))
	
	cv2.waitKey(0)
	
	print(center,radius)
	
	#print(img.shape[0],img.shape[1])
	#im.imread("frame%d.jpg" % count)
"""
	for i in range(int(img.shape[0]/5)):
		for j in range(img.shape[1]):
			
			#go back and make this generalizable
			#these were made into appending blocks to improve performance 
			#i may try to clock runs later to find a better blocking number but first i need to generalizez it
			#also indexing needs to be of just the circle, not the entire image
			if sd.circledetect(5*i,j,center,radius):
				
				r1=np.append(r1,img[5*i][j][0])
				b1=np.append(b1,img[5*i][j][1])
				g1=np.append(g1,img[5*i][j][2])

			if sd.circledetect(5*i+1,j,center,radius):
				
				r2=np.append(r2,img[5*i+1][j][0])
				b2=np.append(b2,img[5*i+1][j][1])
				g2=np.append(g2,img[5*i+1][j][2])
			
			if sd.circledetect(5*i+2,j,center,radius):
				
				r3=np.append(r3,img[5*i+2][j][0])
				b3=np.append(b3,img[5*i+2][j][1])
				g3=np.append(g3,img[5*i+2][j][2])
			
			if sd.circledetect(5*i+3,j,center,radius):
				
				r4=np.append(r4,img[5*i+3][j][0])
				b4=np.append(b4,img[5*i+3][j][1])
				g4=np.append(g4,img[5*i+3][j][2])
			
			if sd.circledetect(5*i+4,j,center,radius):

				r5=np.append(r5,img[5*i+4][j][0])
				b5=np.append(b5,img[5*i+4][j][1])
				g5=np.append(g5,img[5*i+4][j][2])			
			
	#generalize this
	r=np.append(np.append(np.append(r1,r2),np.append(r3,r4)),r5)
	b=np.append(np.append(np.append(b1,b2),np.append(b3,b4)),b5)
	g=np.append(np.append(np.append(g1,g2),np.append(g3,g4)),g5)

	#need to calculate the mean and variance within the circle only 
	mean=[np.mean(r),np.mean(b),np.mean(g)]	
	var=[np.var(r),np.var(b),np.var(g)]
"""

