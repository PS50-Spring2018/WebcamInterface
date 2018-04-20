import time
import cv2
import numpy as np
import CameraOps as co
import ShapeDetector as sd
import csvSave as csvSave
import os
import datetime

class Processor:
	
	def __init__(self, time, interv,rxn_id):
		
		self.reaction_id=rxn_id
	
		self.interv=interv
		self.t  = time
		
		self.count=0

	def run(self):
		
		if not os.path.exists("/Users/shreyamenon/Dropbox/%s" % self.reaction_id):
		
			os.makedirs("/Users/shreyamenon/Dropbox/%s" % self.reaction_id)

		for i in range(int(self.t/self.interv)):
			#runs a single image process
			tempM,tempV=self.iteration()
			
			time.sleep(self.interv/1000) 
			
			#print(tempM,tempV)
			
	def getTime(self):
		
		currentDT = datetime.datetime.now()
		
		time=currentDT.strftime('%Y%m%d%H%M%s')
		
		return time
	
	def iteration(self):
		
		#change to 1 for functionality of the webcam
		initial_img = co.snap(0)

		#name = self.getTime()
		name= self.getTime()

		cv2.imwrite("frame%s.jpg" % name, initial_img)
		#np.save("/Users/shreyamenon/Dropbox/%s/frame%s.npy" % (self.reaction_id,name),initial_img)

		#np.save("frame%s_np.npy" % name,initial_img)
		
		img = cv2.imread("frame%s.jpg" % name)
		#np.save("/Users/shreyamenon/Dropbox/%s/%s.npy" % (self.reaction_id,name),circle)

		#cv2.namedWindow("Display")
		center, radius=sd.detect(sd, img)

		circle=cv2.circle(img,center,radius,(0,255,0),2)
		np.save("/Users/shreyamenon/Dropbox/%s/%s.npy" % (self.reaction_id,name),circle)


		#np.save()
		#cv2.imshow("Display",cv2.circle(img,center,radius,(0,255,0),2))
		#cv2.waitKey(0)
	
		mask=np.zeros((int(img.shape[0]),int(img.shape[1]),3))
	
		left=radius
		right=radius
		top=radius
		bottom=radius

		for i in range(int(radius)):
			delta=int(np.sqrt(int(radius)**2-int(i)**2))
			
			left=delta
			right=delta
			up=i
			down=i

			if mask.shape[0]<center[0]+right:
				
				right=center[0]-mask.shape[0]+1
			if 0>center[0]+up:
				
				left=-center[0]
			if mask.shape[1]<center[1]-down:
				
				down=center[1]-mask.shape[1]+1
			if 0>center[1]+up:
				
				up=-center[1]

			delta=int(np.sqrt(int(radius)**2-int(i)**2))
			
			x=np.arange(int(center[0])-left,int(center[0])+right-1)

			mask[x,(center[1]+up-1),:]=1

			mask[x,(center[1]-down),:]=1
		

		zeros=np.multiply(img,mask)

		masked = np.ma.masked_equal(zeros, 0)

		mean=[np.mean(masked[:,:,0]),np.mean(masked[:,:,1]),np.mean(masked[:,:,2])]
		
		var=[np.var(masked[:,:,0]),np.var(masked[:,:,1]),np.var(masked[:,:,2])]

		csvSave.save(self.reaction_id,name,mean,var)

		return mean,var

		