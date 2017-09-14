import csv, math 

rawResults = open('raw_results.csv')
reader = csv.DictReader(rawResults)

endResults = open('end_results.csv', 'w')
writer = csv.writer(endResults)

def formatSecondsAsString(num): 
	# zfill is a string method that fills out the beginning of string with zeros. Handy! 
	seconds = str(num % 60).zfill(2) 
	minutes = str(math.floor(num/60))

	return ":".join([minutes, seconds])

class President:
	def __init__(self, name, time):
		self.fullName = name
		self.finishTime = time
	def __str__(self): 
		",".join([str(self.fullName), self.finishTime])


for row in reader: 
	name = " ".join([row["first name"], row["last name"]])
	time = formatSecondsAsString(int(row["finish time in seconds"]))

	writer.writerow([name, time])