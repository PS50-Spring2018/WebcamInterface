
import time
import cv2
import numpy as np
import CameraOps as co
import ShapeDetector as sd
import csvSave as csvSave

class Processor:
	def __init__(self, time, interv):
		self.t=time
		self.interv=interv
		self.count=0

	def run(self):
		

		for i in range(int(self.t/self.interv)):
			tempM,tempV=self.iteration()
			cv2.waitKey(self.interv)
			print(tempM,tempV)
			#	here add the csv read out for the mean, var#

	def iteration(self):
		

		initial_img = co.snap(1)

		r1,r2,r3,r4,r5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
		b1,b2,b3,b4,b5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])
		g1,g2,g3,g4,g5=np.array([]),np.array([]),np.array([]),np.array([]),np.array([])

		cv2.imwrite("frame%d.jpg" % self.count, initial_img)

		np.save("frame%d_np.npy" % self.count,initial_img)
		name = time.time()
		
		img = cv2.imread("frame%d.jpg" % self.count)
		
		cv2.namedWindow("Display")
		
		center, radius=sd.detect(sd, img)
		#temp
		center=(100,100)
		radius=20
		cv2.imshow("Display",cv2.circle(img,center,radius,(0,255,0),2))
	
		#enable to test image quality
		#cv2.waitKey(0)
		
		#print(center,radius)

		for i in range(int(img.shape[0]/5)):
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
					g5=np.append(g5,img[5*i+4][j][2])			
				
		r=np.append(np.append(np.append(r1,r2),np.append(r3,r4)),r5)
		b=np.append(np.append(np.append(b1,b2),np.append(b3,b4)),b5)
		g=np.append(np.append(np.append(g1,g2),np.append(g3,g4)),g5)

		mean=[np.mean(r),np.mean(b),np.mean(g)]	
		var=[np.var(r),np.var(b),np.var(g)]

		c = csvSave(name,mean,var,center,radius)
		c.save()
		return mean,var

		self.count+=1