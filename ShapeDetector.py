#remember conda install imutils
import cv2
	
def detect(self, c):
	# initialize the shape name and approximate the contour
	
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.04 * peri, True)

	return approx
