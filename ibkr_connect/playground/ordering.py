from ib_insync import *

ib = IB()

ib.connect('127.0.0.1', 7497, clientId=122)

# contract = Stock('700', 'SEHK', 'HKD')
contract = ContFuture(
    symbol='HSI',
    exchange='HKFE'
)
ib.qualifyContracts(contract)

# Limit Order
# order = LimitOrder('BUY', 2000, 322)
# trade = ib.placeOrder(contract, order)

# Bracket Order
bracket = ib.bracketOrder(action='BUY',
                        quantity=1,
                        limitPrice=19900,
                        takeProfitPrice=21000,
                        stopLossPrice=18800)
for o in bracket:
    ib.placeOrder(contract, o)

ib.sleep(1)

print(ib.trades())

ib.disconnect()
