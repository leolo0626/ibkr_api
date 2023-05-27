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
                            whatToShow='TRADES',
                            useRTH=False,
                            formatDate=1,
                            keepUpToDate=True)


def onBarUpdate(bar, hasNewBar):
    # When the bar update, we can place the signal function here
    # Save the Price data for future update for future checking
    # Ordering is also place here
    # If order is placed, then we may need a messaging channel to notify the user in the group
    if hasNewBar:
        print(bar)


bars.updateEvent += onBarUpdate

# What if we don't cancel it, will it keep update the bar ??
ib.sleep(60)
ib.cancelHistoricalData(bars)

ib.disconnect()
