import time
import cv2
import numpy as np
import CameraOps as co
import ShapeDetector as sd
import csv as csv


class csvSave: 
	def_init_(self,file,mean,variance,cnt,rad):
	self.file = file
	self.mean = mean 
	self.variance = variance
	self.cnt = cnt
	self.rad = rad
	self.countour = [self.center,self.rad] 

	def save(): 
		with open('summary.csv') as csvfile:
    	swriter = csv.writer(csvfile)
   		swriter.writerow(self.file,self.mean,self.variance,self.contour)

