# here will be a list of all api functions we are using as well as a description of how they are used.

# Initializing the client

from binanace.client import Client
client = Client(api_key, api_secret)

# kline websocket, interval automatically set to 1m

from binance.enums import *
conn_key = bm.start_kline_socket('BNBBTC', process_message, interval=KLINE_INTERVAL_30MINUTE)

# Get margin price index

info = client.get_margin_price_index(symbol='BTCUSDT')

# place a margin order

from binance.enums import *
order = client.create_margin_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=100,
    price='0.00001')

# order status 

order = client.get_margin_order(
    symbol='BNBBTC',
    orderId='orderId')

# Cancel order

result = client.cancel_margin_order(
    symbol='BNBBTC',
    orderId='orderId')

# Place a limit order

order = client.order_limit_buy(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')

order = client.order_limit_sell(
    symbol='BNBBTC',
    quantity=100,
    price='0.00001')

# get asset balance

balance = client.get_asset_balance(asset='BTC')

# get trades

trades = client.get_my_trades(symbol='BNBBTC')

# get trade fees
# get fees for all symbols
fees = client.get_trade_fee()

# get fee for one symbol
fees = client.get_trade_fee(symbol='BNBBTC')

# withdraw

from binance.exceptions import BinanceAPIException, BinanceWithdrawException
try:
    # name parameter will be set to the asset value by the client if not passed
    result = client.withdraw(
        asset='ETH',
        address='<eth_address>',
        amount=100)
except BinanceAPIException as e:
    print(e)
except BinanceWithdrawException as e:
    print(e)
else:
    print("Success")

# passing a name parameter
result = client.withdraw(
    asset='ETH',
    address='<eth_address>',
    amount=100,
    name='Withdraw')

# if the coin requires a extra tag or name such as XRP or XMR then pass an `addressTag` parameter.
result = client.withdraw(
    asset='XRP',
    address='<xrp_address>',
    addressTag='<xrp_address_tag>',
    amount=10000)
