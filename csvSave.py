import csv as csv
	
def save(rxnID,file,mean,variance):
	#with open('summary_%s.csv' % rxnID, 'a+') as csvfile:
	### make 'folder' an argument
	#folderwoID = '/Users/shreyamenon/Dropbox/'
	folderwoID = '/Users/tim/Google Drive/Teaching/'
	with open(folderwoID+'%s/summary_%s.csv' % (rxnID,rxnID),'a+') as csvfile:
		swriter = csv.writer(csvfile)
		swriter.writerow([file, mean[0],mean[1],mean[2], variance[0],variance[1],variance[2]])

