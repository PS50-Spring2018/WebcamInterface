import csv as csv
	
def save(file,mean,variance): 

	with open('summary.csv','w+') as csvfile:
	
		swriter = csv.writer(csvfile)
	
		swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])

