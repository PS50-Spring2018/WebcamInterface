import time
import cv2
import numpy as np
import CameraOps as co
import ShapeDetector as sd
import csvSave as csvSave
import os
import datetime
import matplotlib.pyplot as plt


if __name__=='__main__':
	
	st='2018042016161524255371.npy'
	img=np.load(st)
	plt.figure()
	plt.imshow(img)
	plt.show()
	#cv2.namedWindow("Display")
	#cv2.imshow("Display",img)
	#cv2.waitKey(0)



