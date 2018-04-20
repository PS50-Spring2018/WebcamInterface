# Example for how to use the opencv module to campure webcam images

# Import opencv
"""import cv2
import numpy as np
import ShapeDetector as sd
import CameraOps as co
from matplotlib import image as im"""
from Processor import Processor
# Function for displaying continuous video stream
# n: Camera number on computer (usually n=0 for built-in webcam)
# Exit video by clicking into video and pressing ESC key



if __name__=='__main__':

<<<<<<< HEAD
	#Uncomment to take single snap
	#add n in the future to distinguish images from one another, this might be a time 
	
	# stream()
	
	s = co.snap(0)
	count=0
	
	r=[]
	b=[]
	g=[]
	
	#derived frmo https://www.pyimagesearch.com/2016/02/08/opencv-shape-detection/
	cv2.imwrite("frame%d.jpg" % count, s) 
	
	img = cv2.imread("frame%d.jpg" % count)
	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	blur = cv2.GaussianBlur(gray, (5, 5), 0)

	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]
=======
>>>>>>> be9ef27867c95d5b7b2ea4684975d4a083855868
	
	#co.stream(1)
	#change this to 1 to use the webcam

	#get user input for time, interv
	time=int(float(input("How long would you like to analyze for? ")))
	
	interv=int(float(input("How often do you want to check? ")))
	#constructor
	p=Processor(time,interv)
	#this function  runs all iterations of the processor class
	p.run()
