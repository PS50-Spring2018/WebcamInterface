
import time
import cv2
import numpy as np
import CameraOps as co
import ShapeDetector as sd
import csvSave as csvSave


if __name__=='__main__':
	
	initial_img = co.snap(0)

	

	cv2.imwrite("test.jpg", initial_img)

	np.save("test.jpg",initial_img)
	
	img = cv2.imread("test.jpg" )
	white=cv2.imread("white.jpg")
	cv2.namedWindow("Display")
	cv2.namedWindow("Cont")
	

	gray = cv2.cvtColor(initial_img, cv2.COLOR_BGR2GRAY)
	#print(gray)
	blur = cv2.GaussianBlur(gray, (5, 5), 0)
	#print(blur)
	thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]



	_, cont,hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


	cv2.imshow("Display",img)
	cv2.waitKey(5000)
	for i in range(len(cont)):
		cv2.imshow("Cont",cv2.drawContours(white, cont, i, (0,255,0), 8))
		center,radii=sd.circle(cont[i])
		cv2.imshow("Cont",cv2.circle(white,center,radii,(0,255,0),2))
		cv2.waitKey(0)