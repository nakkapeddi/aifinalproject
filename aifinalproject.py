import sys
import datadumper
import pickle
import math


print """Generating dataset (historical stock data)..."""
datadumper.data_dump()

myList = []
stockFile = open('historicaldata.pickle', 'r')
while 1:
    try:
        myList.append(pickle.load(stockFile))
    except (EOFError):
        break
stockFile.close()

for index1, row in enumerate(myList):
	for index2, item in enumerate(row):
		try:
			myList[index1][index2] = (math.log(float(item)))
		except ValueError:
			pass
print myList
