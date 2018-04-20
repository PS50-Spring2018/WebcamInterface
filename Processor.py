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

		self.t=time
		
		self.interv=interv
		
		self.count=0

	def run(self):
		
		if not os.path.exists("/Users/shreyamenon/Dropbox/%s" % self.reaction_id):
			os.makedirs("/Users/shreyamenon/Dropbox/%s" % self.reaction_id)

		for i in range(int(self.t/self.interv)):
			#runs a single image process
			tempM,tempV=self.iteration()
			#waits for the determined intercal
			#time.sleep here
			#cv2.waitKey(self.interv)
			#prints output,supress post testing
			print(tempM,tempV)
			
	def getTime(self):
		currentDT = datetime.datetime.now()
		time = currentDT.strftime('%Y%m%d%H%M%s')
		return time
	
	def iteration(self):
		
		#change to 1 for functionality of the webcam
		initial_img = co.snap(0)

		name = self.getTime()

		cv2.imwrite("frame%s.jpg" % name, initial_img)

		np.save("/Users/shreyamenon/Dropbox/%s/%s.npy" % (self.reaction_id,name),initial_img)
		#np.save("frame%s_np.npy" % name,initial_img)
		
		img = cv2.imread("frame%s.jpg" % name)
		
		#cv2.namedWindow("Display")
		
		center, radius=sd.detect(sd, img)
		print(center,radius)
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
			if mask.shape[0]>center[0]-left:
				left=center[0]
			if mask.shape[1]<center[1]-down:
				down=center[1]-mask.shape[1]+1
			if mask.shape[1]>center[1]+up:
				up=-center[1]

			delta=int(np.sqrt(int(radius)**2-int(i)**2))
			x=np.arange(int(center[0])-left,int(center[0])+right)
			mask[x,(center[1]+up),:]=1
			mask[x,(center[1]-down),:]=1
		

		zeros=np.multiply(img,mask)
		masked = np.ma.masked_equal(zeros, 0)

		mean=[np.mean(masked[:,:,0]),np.mean(masked[:,:,1]),np.mean(masked[:,:,2])]
		var=[np.var(masked[:,:,0]),np.var(masked[:,:,1]),np.var(masked[:,:,2])]

		csvSave.save(self.reaction_id,name,mean,var)

		return mean,var

		self.count+=1

		
		"""
		r1,r2,r3,r4,r5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
		b1,b2,b3,b4,b5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
		g1,g2,g3,g4,g5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
		
		#create a mask with 0/1 as being the points iin the  circle or outside them 
		#multiply the 

		for i in range(int(img.shape[0]/5)):
									
									print("*",end="")
									for j in range(img.shape[1]):		
										#go back and make this generalizable
										#these were made into appending blocks to improve performance 
										#i may try to clock runs later to find a better blocking number but first i need to generalizez it
										#also indexing needs to be of just the circle, not the entire image
										if sd.circledetect(5*i,j,center,radius):
											
											r1=np.append(r1,img[5*i][j][0])
											b1=np.append(b1,img[5*i][j][1])
											g1=np.append(g1,img[5*i][j][2])
						
										if sd.circledetect(5*i+1,j,center,radius):
											
											r2=np.append(r2,img[5*i+1][j][0])
											b2=np.append(b2,img[5*i+1][j][1])
											g2=np.append(g2,img[5*i+1][j][2])
										
										if sd.circledetect(5*i+2,j,center,radius):
											
											r3=np.append(r3,img[5*i+2][j][0])
											b3=np.append(b3,img[5*i+2][j][1])
											g3=np.append(g3,img[5*i+2][j][2])
										
										if sd.circledetect(5*i+3,j,center,radius):
											
											r4=np.append(r4,img[5*i+3][j][0])
											b4=np.append(b4,img[5*i+3][j][1])
											g4=np.append(g4,img[5*i+3][j][2])
										
										if sd.circledetect(5*i+4,j,center,radius):
						
											r5=np.append(r5,img[5*i+4][j][0])
											b5=np.append(b5,img[5*i+4][j][1])
											g5=np.append(g5,img[5*i+4][j][2])			"""
				
		"""r=np.append(np.append(np.append(r1,r2),np.append(r3,r4)),r5)
			b=np.append(np.append(np.append(b1,b2),np.append(b3,b4)),b5)
			g=np.append(np.append(np.append(g1,g2),np.append(g3,g4)),g5)"""
