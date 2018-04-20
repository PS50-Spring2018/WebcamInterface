import time
import cv2
import numpy as np
import CameraOps as co
import ShapeDetector as sd
import csv as csv
	
def save(file,mean,variance): 
	with open('summary.csv','a+') as csvfile:
		swriter = csv.writer(csvfile)
		swriter.writerow([file, mean, variance])

