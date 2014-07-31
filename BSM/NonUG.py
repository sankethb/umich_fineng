import os, re, subprocess
import fileinput, time
import argparse
import fnmatch
import tick_pb2 as proto
import varint
import csv



def getInstrumentIterator(pricedFile, instrumentFilter=None):

	# Loop to read each pricedData object in the file

	pricedData = []
	lastOptionMeta = None

	for pricedRecord in readProto(pricedFile):
		optionMeta = pricedRecord.pairedTick.optionMeta

		if lastOptionMeta:
			if lastOptionMeta.instrument !=  optionMeta.instrument:
				if len(pricedData) > 0:
					yield (lastOptionMeta, pricedData)
				pricedData = []

		lastOptionMeta = optionMeta

		if instrumentFilter and optionMeta.instrument not in instrumentFilter:
			continue


		pricedData.append(pricedRecord)

	if len(pricedData) > 0:
		yield (lastOptionMeta, pricedData)


def readProto(pricedFile):
	inputFh = open(pricedFile, "rb")
	data  = inputFh.read()
	decoder = varint.decodeVarint32
	next_pos, pos = 0, 0
	while 1:
		pricedRecord = proto.PricedRecord()

		try:
			next_pos, pos = decoder(data, pos)
		except:
			break
		pricedRecord.ParseFromString(data[pos:pos + next_pos])
		yield pricedRecord
		pos += next_pos
	inputFh.close()


def getTimeInSecs(timeStr):
	time = map(lambda x: int(x),  timeStr.split(':'))
	timeSecs = (time[0] * 24 * 60) + (time[1] * 60) + time[2]
	return timeSecs


def createPositions(pricedData):
	positionsIndex = []

	startPositionIndex = None
	endPositionIndex = None

	i = 0
	for pricedRecord in pricedData:
		timeSecs = getTimeInSecs(pricedRecord.pairedTick.optionTick.timestampStr.split(' ')[1])

		if not startPositionIndex:
			if timeSecs > getTimeInSecs('09:00:00'):
				startPositionIndex = i

		if not endPositionIndex:
			if timeSecs > getTimeInSecs('16:00:00'):
				endPositionIndex = i
				break

		i = i + 1

	if startPositionIndex and endPositionIndex:
		positionsIndex.append((startPositionIndex, endPositionIndex))

	return positionsIndex

def processPosition(optionMeta, pricedData, positionIndex):
	(startPositionIndex, endPositionIndex) = positionIndex
        print positionIndex
        a = positionIndex[0]
        b = positionIndex[1] + 1
        print a
        #print pricedData.pairedTick[35].TimstampStr.split(' ')[1]        
        NonUniGridData = []
        counter = 0            
        writer = csv.writer(open('sankethlist.csv','wb'))
        writer.writerow(['instrument', 'timestamp','id', 'deviation', 'empirical delta', 'theoretical delta', 'gamma', 'stockLast'])
	for p in range(a,b):
            print p
            
            timeSecsCurrent = getTimeInSecs(pricedData[p].pairedTick.optionTick.timestampStr.split(' ')[1])
            timeSecsPrevious = getTimeInSecs(pricedData[p-1].pairedTick.optionTick.timestampStr.split(' ')[1])
            timeDiff = timeSecsCurrent-timeSecsPrevious
            if timeDiff < getTimeInSecs('00:05:00'):
                counter = counter + 1
            else:
                if counter == 1:                    
                    pricedRecord_t0 = pricedData[counter-1]
                    pricedRecord_t1 = pricedData[counter]
                    prpRecord = pricedRecord_t1

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
                        prpRecord = pricedRecord_t2
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

                        NonUniGridData.append({'Timestamp' : prpRecord.pairedTick.optionTick.timestamp,
                                   'Instrument': optionMeta.instrument,
                                   'OptionPrice': callPrice,
                                   'UnderlyingPrice': underlyingPrice,
                                   'NUGdelta': observedDelta,
                                   })
                        print NonUniGridData
#                else if counter >= 3
#                    pricedRecord_t0 = pricedData[counter-3]
#                    pricedRecord_t1 = pricedData[counter-2]
#                    pricedRecord_t2 = pricedData[counter-1]
#                    pricedRecord_t3 = pricedData[counter]
#
#                    underlyingTick_t0 = pricedRecord_t0.pairedTick.underlyingTick
#                    underlyingTick_t1 = pricedRecord_t1.pairedTick.underlyingTick
#                    underlyingTick_t2 = pricedRecord_t2.pairedTick.underlyingTick
#                    underlyingTick_t3 = pricedRecord_t3.pairedTick.underlyingTick
#
#                    optionTick_t0 = pricedRecord_t0.pairedTick.optionTick
#                    optionTick_t1 = pricedRecord_t1.pairedTick.optionTick
#                    optionTick_t2 = pricedRecord_t2.pairedTick.optionTick
#                    optionTick_t3 = pricedRecord_t3.pairedTick.optionTick	           	           
#
#
#                    underlyingLastDiff = (underlyingTick_t0.ask - underlyingTick_t1.ask) + (underlyingTick_t0.bid - underlyingTick_t1.bid)
#                    optionLastDiff = (optionTick_t0.ask - optionTick_t1.ask) + (optionTick_t0.bid - optionTick_t1.bid)
#
#                    distOne = ((underlyingTick_t1.last - underlyingTick_t0.last) + (underlyingTick_t1.bid - underlyingTick_t0.bid))/2
#                    distTwo = ((underlyingTick_t2.ask - underlyingTick_t1.ask) + (underlyingTick_t2.bid - underlyingTick_t1.bid))/2
#                
#                    distOne = (underlyingTick_t1.last - underlyingTick_t0.last) 
#                    distTwo = (underlyingTick_t2.last - underlyingTick_t1.last)
#
#                    underlyingLastDiff = (underlyingTick_t1.last - underlyingTick_t0.last)
#                    optionLastDiff = (optionTick_t1.last - optionTick_t0.last)
#                    
#                    underlyingLastDiff = underlyingTick_t0.last - underlyingTick_t1.last
#                    optionLastDiff = optionTick_t0.last - optionTick_t1.last
#                    
#                    Skipping deltas that have experienced no change
#                    if underlyingLastDiff == 0 or optionLastDiff == 0:
#                        print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (i, i + 1)
#                        continue
#
#                    if distOne == 0 or distTwo == 0:
#                        print 'Skipping delta calculation at index (%d,%d), due to no change in quotes' % (i, i + 1)
#                        continue
#                    
#                    observedDelta = optionLastDiff/underlyingLastDiff
#                
#                    opt_t0 = (optionTick_t0.ask + optionTick_t0.bid)/2                
#                    opt_t1 = (optionTick_t1.ask + optionTick_t1.bid)/2
#                    opt_t2 = (optionTick_t2.ask + optionTick_t2.bid)/2
#                    
#                    opt_t0 = optionTick_t0.last                
#                    opt_t1 = optionTick_t1.last
#                    opt_t2 = optionTick_t2.last
#                
#                    observedCentralDelta = (opt_t2 - ((distTwo/distOne)**2)*opt_t0 - (1 - (distTwo/distOne)**2)*opt_t1)/(distTwo*(1 + (distTwo/distOne)))
#                    observedCentralDelta2 = ((-distTwo)/((distOne)*(distOne + distTwo)))*opt                            
#                    
#                    observedGamma = 2*(opt_t2 + (distTwo/distOne)*opt_t2 - (1+(distTwo/distOne))*opt_t1)/(distOne*distTwo*(1 + (distTwo/distOne)))
                           
def processInstrument(optionMeta, pricedData):
	print 'Processing -', optionMeta

	positions = createPositions(pricedData)
        print positions
        raw_input("Enter to continue")
	if len(positions) == 0:
		print 'No positions found'
		return 

	print "Found positions"
	for positionIndex in positions:
		processPosition(optionMeta, pricedData, positionIndex)



def main():
    
    print 'check'
    for root, dirnames, filenames in os.walk("C://Trading//data//analysis_20140628//FDX.priced//FDX//FDX//20140610"):
    	for filename in fnmatch.filter(filenames, 'option_tick_priced.proto'):
    		pricedDataFile = root + "/" + filename
    		print 'Processing file -', pricedDataFile 
    		for (optionMeta, pricedData) in getInstrumentIterator(pricedDataFile,('FDX1421F145')):
    			processInstrument(optionMeta, pricedData)
    			break
                      


if __name__ == "__main__":
    main()
