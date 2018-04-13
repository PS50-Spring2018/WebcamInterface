# Example for how to use the opencv module to campure webcam images

# Import opencv
import cv2
import time
import numpy as np

# Function for displaying continuous video stream
# n: Camera number on computer (usually n=0 for built-in webcam)
# Exit video by clicking into video and pressing ESC key
def stream(n=0):
	cv2.namedWindow("preview")
	vc = cv2.VideoCapture(n)

	if vc.isOpened(): # try to get the first frame
	    rval, frame = vc.read()
	    print('frame\n', frame[0][:])
	else:
	    rval = False
	    frame = None

	while rval:
	    cv2.imshow("preview", frame)
	    rval, frame = vc.read()
	    key = cv2.waitKey(20)
	    if key == 27: # exit on ESC
	        break

	cv2.destroyWindow("preview")
	vc.release()
	
# Function taking a single picture from webcam and returning it in array form
# n: Camera number on computer (usually n=0 for built-in webcam)
def snap(n=0):
	cv2.namedWindow("preview")
	vc = cv2.VideoCapture(n)

	if vc.isOpened(): # try to get the first frame
	    rval, frame = vc.read()
	    print('frame\n', frame[0][:])
	else:
	    rval = False
	    frame = None

	cv2.destroyWindow("preview")
	vc.release()
	#frame=np.array(frame)
	#print('size', np.shape(frame))
	return frame


if __name__=='__main__':

	# #Uncomment to stream webcam video
	#stream()

	# #Uncomment to take single snap
	##print(s)














