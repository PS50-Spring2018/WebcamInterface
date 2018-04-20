import csv as csv
	
def save(id,file,mean,variance): 
#<<<<<<< HEAD
	with open('summary.csv','a+') as csvfile:

		swriter = csv.writer(csvfile)
	
		swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])

