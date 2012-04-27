#!/usr/bin/env python
#
#  Copyright (c) 2012, Naveen Akkapeddi (naveen.csci@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#  

import sys
import datadumper
import pickle
import math
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer, SoftmaxLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

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
#print targetData

myNet = buildNetwork(2, 2, 1, hiddenclass=TanhLayer, outclass=SoftmaxLayer) # Build network with 2 input neurons, 2 hidden neurons, and 1 output neuron
print myNet['in'], myNet['hidden0'], myNet['out']

myDS = SupervisedDataSet(2, 1) # Create dataset with two dimensional input, one dimensional target.

for i in enumerate(myList): #Pop off each element, then added to dataset
	myDataSetAdder = myDS.appendLinked(myList.pop(), targetData.pop())

for inpt, target in myDS: #display dataset structure
	print inpt, target

myTrainer = BackpropTrainer(myNet, myDS)
print """This may take awhile..."""
myTrainData, myTestData = myDS.splitWithProportion(0.25)
print len(myTrainData), len(myTestData)
print myTrainer.train() #TODO, setup network structure differently.
