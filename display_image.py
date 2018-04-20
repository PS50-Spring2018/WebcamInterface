import time
import cv2
import numpy as np
import CameraOps as co
import ShapeDetector as sd
import csvSave as csvSave
import os
import datetime


if __name__=='__main__':
	
	st=''
	img=np.load(st)
	cv2.namedWindow("Display")
	cv2.imshow("Display",img)
	cv2.waitKey(0)



