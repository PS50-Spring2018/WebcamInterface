import csv as csv
	
def save(rxnID,file,mean,variance):
	with open('summary%d.csv' % rxnID,'a+') as csvfile:
		swriter = csv.writer(csvfile)
		swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])

