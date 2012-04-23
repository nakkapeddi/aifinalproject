import sys
import datadumper
import pickle
import math


print """Generate dataset (historical stock data)?
1) Yes
2) No"""
answer = raw_input("> ")

if "1" in answer: datadumper.data_dump()
elif "2" in answer: print 'Continuing...'

myList = []
stockFile = open('historicaldata.pickle', 'r')
while 1:
    try:
        myList.append(pickle.load(stockFile))
    except (EOFError):
        break
stockFile.close()

priceVol = myList.pop()
floatPriceVol = [float(integral) for integral in priceVol]
vol = floatPriceVol.pop()
price = floatPriceVol.pop()

logPrice = math.log(price)
