# Example for how to use the opencv module to campure webcam images

# Import opencv
import cv2
import numpy as np
import ShapeDetector as sd
import CameraOps as co


# Function for displaying continuous video stream
# n: Camera number on computer (usually n=0 for built-in webcam)
# Exit video by clicking into video and pressing ESC key



if __name__=='__main__':

	#Uncomment to take single snap
	#add n in the future to distinguish images from one another, this might be a time 
	
	#change this to 1 to use the webcam
	s = co.snap(0)
	count=0
	
	r=[]
	b=[]
	g=[]
	

	#derived from https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
	cv2.imwrite("frame%d.jpg" % count, s) 
	np.save("frame%d_np.npy" % count,s)

	
	img = cv2.imread("frame%d.jpg" % count)
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	blur = cv2.GaussianBlur(gray, (5, 5), 0)

	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
	
	cont=sd.detect(thresh)

	center=[]
	radii=[]

	for line in cont:

		temp=circle(line)
		
		center.append(temp[0])
		
		radii.append(temp[1])
	
	radii=np.array(radii)
	
	ind=np.argmax(radii)

	beaker=center[ind],radius[ind]

	print(beaker[0],beaker[1])

	for i in range(s.shape[0]):
	
		for j in range(s.shape[1]):
						
			r.append(s[i][j][0])

			b.append(s[i][j][1])
			
			g.append(s[i][j][2])
					
			
			r=np.array(r)
			
			b=np.array(b)
			
			g=np.array(g)
	
			mean=[np.mean(r),np.mean(b),np.mean(g)]
			
			var=[np.var(r),np.var(b),np.var(g)]

