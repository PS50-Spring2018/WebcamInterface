import csv as csv
	
#<<<<<<< HEAD
def save(id,file,mean,variance): 
#<<<<<<< HEAD
	with open('summary.csv','a+') as csvfile:

#=======
#def save(rxnID,file,mean,variance):
	#with open('summary_%s.csv' % rxnID, 'a+') as csvfile:
#	with open('/Users/shreyamenon/Dropbox/%s/summary_%s.csv' % (rxnID,rxnID),'a+') as csvfile:
#>>>>>>> 6bbc8fac0b6c8f0c657a31e79d6c29f267bc29b3
		swriter = csv.writer(csvfile)
		swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])

