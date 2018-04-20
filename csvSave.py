import csv as csv
	
def save(file,mean,variance): 
<<<<<<< HEAD
	with open('summary.csv','a+') as csvfile:
=======

	with open('summary.csv','a') as csvfile:
	
>>>>>>> ffd1074038f19950ecd3c7e6fba2915f780237d5
		swriter = csv.writer(csvfile)
	
		swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])

