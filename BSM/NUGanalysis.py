import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import tick_pb2 as proto
import varint
import csv
import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import matplotlib.pyplot as plt
import math, pandas
import time
import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import matplotlib.pyplot as plt
import math, pandas
import time
import tick_pb2 as proto
import utils
import varint
import itertools
import numpy as np
from profitAndLoss import *
from positions import createPositions
from BSManalysis import *
from readProto import getInstrumentIterator
from utils import getTimeGMTFromUTCEpoch, getTimeInSecs, getInstrumentMetaStr
import itertools
import numpy as np
from profitAndLoss import *
from positions import createPositions
from BSManalysis import *

def computeDiffeqnValues(optionMeta,pricedData, positionIndex):
    NonUniGridData = []
    for pricedRecord in pricedData:
        (startPositionIndex, endPositionIndex) = positionIndex
        print positionIndex
        a = positionIndex[0]
        b = positionIndex[1] + 1
        print a
        counter = 0 
        for p in range(a,b):
            timeSecsCurrent = getTimeInSecs(pricedData[p].pairedTick.optionTick.timestampStr.split(' ')[1])
            timeSecsPrevious = getTimeInSecs(pricedData[p-1].pairedTick.optionTick.timestampStr.split(' ')[1])
            timeDiff = timeSecsCurrent-timeSecsPrevious
            if timeDiff < getTimeInSecs('00:10:00'):
                counter = counter + 1
            else:
                if counter == 1:                    
                    pricedRecord_t0 = pricedData[counter-1]
                    pricedRecord_t1 = pricedData[counter]

                    underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
                    underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
                
                    optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
                    optionTick_t1 = pricedRecord_t1.pairedTick.optionTick

                    underlyingLastDiff = (underlyingTick_t1.last - underlyingTick_t0.last)
                    optionLastDiff = (optionTick_t1.last - optionTick_t0.last)

                    if underlyingLastDiff == 0 or optionLastDiff == 0:
                        print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (p, p + 1)
                        continue

   #                 if distOne == 0 or distTwo == 0:
			#print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (i, i + 1)
			#continue

                    observedDelta = optionLastDiff/underlyingLastDiff
                    #observedGamma = 
                    underlyingPrice = pricedRecord_t1.pairedTick.underlyingTick.last
                    callPrice = pricedRecord_t1.pairedTick.optionTick.last
                    interestRate = pricedRecord_t1.pairedTick.interestRate 
                    daysToExpiration = pricedRecord_t1.pairedTick.daysToExpire
                    strikePrice = pricedRecord_t1.pairedTick.optionMeta.strike

                else: 
                    if counter >= 2:   
                        pricedRecord_t0 = pricedData[counter-2]
                        pricedRecord_t1 = pricedData[counter-1]
                        pricedRecord_t2 = pricedData[counter]

                        underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
                        underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
                        underlyingTick_t2 = pricedRecord_t2.pairedTick.underlyingTick

                        optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
                        optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
                        optionTick_t2 = pricedRecord_t2.pairedTick.optionTick

                        a = underlyingTick_t2.last - underlyingTick_t1.last
                        b = underlyingTick_t2.last - underlyingTick_t0.last
                        
                                             
                        denominator = (a*b*(b-a))
                        numerator = (pow(a,2)*optionTick_t0.last - pow(b,2)*optionTick_t1.last + (pow(b,2) - pow(a,2))*optionTick_t2.last)

                        if numerator == 0 or denominator == 0:
                            print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (p, p + 1)
                            continue
                       
                        observedDelta = numerator/denominator
                                                
                        observedGamma = ((-a*optionTick_t0.last + b*optionTick_t1.last - (b-a)*optionTick_t2.last)*-2)/denominator
                
                        underlyingPrice = pricedRecord_t2.pairedTick.underlyingTick.last
                        callPrice = pricedRecord_t2.pairedTick.optionTick.last
                        interestRate = pricedRecord_t2.pairedTick.interestRate 
                        daysToExpiration = pricedRecord_t2.pairedTick.daysToExpire
                        strikePrice = pricedRecord_t2.pairedTick.optionMeta.strike        
                        
                theoDelta = []
                theoPrice = []
           
                for theoretical in pricedRecord.theoreticals:
                    theoDelta.append(theoretical.delta)
                    theoPrice.append(theoretical.price)
                NonUniGridData.append({'Timestamp' : pricedRecord.pairedTick.optionTick.timestamp,
                        'Instrument': optionMeta.instrument,
                        'OptionPrice': callPrice,
                        'UnderlyingPrice': underlyingPrice,
                        'BSMdelta': BSdelta,
                        'TheoreticalDeltaMin':min(theoDelta),
                        'TheoreticalDeltaMax':max(theoDelta),
                        'BSMprice' : BSprice,
                        'TheoreticalPriceMin': min(theoPrice),
                        'TheoreticalPriceMax': max(theoPrice) 
                        })