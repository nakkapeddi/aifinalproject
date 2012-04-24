import sys
import datadumper
import pickle
import math
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer, SoftmaxLayer
from pybrain.datasets import SupervisedDataSet

print """Generating dataset (historical stock data)..."""
datadumper.data_dump()

myList = [] 	# Create empty list to store nested list containing closing price and volume
stockFile = open('historicaldata.pickle', 'r')
while 1:
    try:
        myList.append(pickle.load(stockFile))
    except (EOFError):
        break
stockFile.close()

for index1, row in enumerate(myList): # For each item in every row of the nested list, convert string to float and apply natural log function
	for index2, item in enumerate(row):
		try:
			myList[index1][index2] = (math.log(float(item)))
		except ValueError:
			pass
#print myList

myClonedList = myList # Alias the previous nested list, take the first item (natural log closing price) of every row and append it to new list.
targetData = []
for index1, row in enumerate(myClonedList):
	targetData.append(myClonedList[index1][0])

targetData.pop() #Pop off last element because it should be the next day's closing price.
print targetData

myNet = buildNetwork(2, 2, 1, hiddenclass=TanhLayer, outclass=SoftmaxLayer) # Build network with 2 input neurons, 2 hidden neurons, and 1 output neuron
print myNet['in'], myNet['hidden0'], myNet['out']

myDS = SupervisedDataSet(2, 1) # Create dataset with two dimensional input, one dimensional target.

for i in range(len(myList)):
	tupleList = tuple(myList[i])
	tupleTarget = tuple(targetData)
	print tupleList, tupleTarget
#	myDS.addSample(tupleList, (0,))
