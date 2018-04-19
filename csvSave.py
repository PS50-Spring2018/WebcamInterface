import csv as csv
	
def save(file,mean,variance): 

	with open('summary.csv','w+') as csvfile:
	
		swriter = csv.writer(csvfile)
	
		swriter.writerow([file, mean, variance])

