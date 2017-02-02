import csv

d = open ('peedata3.csv','U')

csv_d = csv.reader(d)

for row in csv_d:
	print row[2]


d.close()
