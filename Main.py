
from Processor import Processor

# Function for displaying continuous video strea
# n: Camera number on computer (usually n=0 for built-in webcam)
# Exit video by clicking into video and pressing ESC key



if __name__=='__main__':

	
	#co.stream(1)
	#change this to 1 to use the webcam

	#get user input for time, interv
	reaction_id=input("What is the reaction ID? ")

	time=int(float(input("How long would you like to analyze for (s)? ")))
	
	interv=int(float(input("How often do you want to check(s)? ")))
	#constructor
	p=Processor(time,interv,reaction_id)
	#this function  runs all iterations of the processor class as defined by the tine and interval
	
	dropbox_dir = "/Users/shreyamenon/Dropbox"
	#dropbox directory

	p.run()
	