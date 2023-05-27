from ib_insync import *

util.startLoop()

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=14)

# contract = ContFuture(
#     symbol='HSI',
#     exchange='HKFE'
# )
contract = Stock('700', 'SEHK', 'HKD')

bars = ib.reqHistoricalData(contract,
                            endDateTime='',
                            durationStr='600 S',
                            barSizeSetting='1 min',
                            whatToShow='ADJUSTED_LAST',
                            useRTH=False,
                            formatDate=1,
                            keepUpToDate=True)


def onBarUpdate(bar, hasNewBar):
    if hasNewBar:
        print(bar)


bars.updateEvent += onBarUpdate

ib.sleep(60)
ib.cancelHistoricalData(bars)

ib.disconnect()
