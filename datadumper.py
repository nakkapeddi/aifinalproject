#!/usr/bin/env python
#
#  Copyright (c) 2012, Naveen Akkapedd (naveen.csci@gmail.com)
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
import ystockquote
import pickle

def data_dump():
	stockData = ystockquote.get_historical_prices('GOOG', 20100901, 20110901) #import stock data from 09/01/2010 to 09/01/2011, format is YYYYMMDD
	f = open('historicaldata.pickle', 'w')
	for line in stockData:
		pickle.dump(line[4:6], f)
	f.close()
