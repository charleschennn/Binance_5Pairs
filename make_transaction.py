from Utilities import calculate_profit
from Utilities import initialize_api as client
from Utilities import bidPrice_and_askPrice
from Utilities import trading_rule_amount_BNB
from Utilities import trading_rule_amount_BTC
from Utilities import trading_rule_amount_ETH
from Utilities import trading_rule_amount_USDT
from Utilities import trading_rule_price_BNB
from Utilities import trading_rule_price_BTC
from Utilities import trading_rule_price_ETH
from Utilities import trading_rule_price_USDT
import time
import threading
import global_var

lock = threading.Lock()

def transaction1(initial_cost, X, main_currency ):

    global lock
    global amount_x_from_main
    global run_second_or_not

    lock.acquire()

    # X_to_main = bidPrice_and_askPrice(X, main_currency)

    price = bidPrice_and_askPrice(X, main_currency)[1]

    print("(1) expected PRICE BEFORE following the Binance rule : {} ".format(price))
    if main_currency == 'BNB':
        price = trading_rule_price_BNB(X, price)
    elif main_currency == 'BTC':   
        price = trading_rule_price_BTC(X, price)
    elif main_currency == 'ETH':
        price = trading_rule_price_ETH(X, price)
    elif main_currency == 'USDT':
        price = trading_rule_price_USDT(X, price)

    print("(1) expected PRICE AFTER following the Binance rule : {} ".format(price))
    
    amount_x_from_main = initial_cost / float(price)

    print("(1) expected AMOUNT BEFORE following the Binance rule : {} ".format(amount_x_from_main))

    if main_currency == 'BNB':
        amount_x_from_main = trading_rule_amount_BNB(X, amount_x_from_main)
    elif main_currency == 'BTC':   
        amount_x_from_main = trading_rule_amount_BTC(X, amount_x_from_main)
    elif main_currency == 'ETH':
        amount_x_from_main = trading_rule_amount_ETH(X, amount_x_from_main)
    elif main_currency == 'USDT':
        amount_x_from_main = trading_rule_amount_USDT(X, amount_x_from_main)
        
    print("(1) expected AMOUNT AFTER following the Binance rule : {} ".format(amount_x_from_main))

    print("(1) buying {} amount of {} using {} {} ".format(amount_x_from_main, X, float(price) * float(amount_x_from_main), main_currency))

    symbol = X + main_currency
    order = client().order_limit_buy (
        symbol= symbol,
        quantity=float(amount_x_from_main),
        price= price
    )

    # place a test market buy order, to place an actual order use the create_order function
    # order = client.create_test_order (
    # symbol= symbol[0]+'USDT',
    # side=Client.SIDE_BUY,
    # type=Client.ORDER_TYPE_LIMIT,
    # quantity=amount_x_from_main,
    # timeInForce= "GTC",
    # price=price  )

    print("(1) checking if the order is filled or not.... ")

    while True:
        
        existing_order = client().get_order(symbol=symbol, orderId=order['orderId'])

        if( existing_order['status'] == "FILLED" ):
            
            break

        else:
            time.sleep(0.05)
        
    print("(1) FILLED")

    transaction_fee = 0

    if X == "BNB" or main_currency == "BNB":
        transaction_fee = format(float(amount_x_from_main) * 0.00075, '.8f')
        amount_x_from_main = float(amount_x_from_main) * 0.99925
    # else:
    # transaction_fee = format(float(amount_x_from_main) * 0.001, '.8f')
    # amount_x_from_main = float(amount_x_from_main) * 0.999

    print("end of transaction 1")
    lock.release()


def transaction2(X, mid_currency ):

    time.sleep(0.05)

    global lock
    global amount_x_from_main
    global amount_mid_from_x

    lock.acquire()

    start = time.time()

    price = bidPrice_and_askPrice(X, mid_currency)[0]
    print("(2) expected PRICE BEFORE following the Binance rule : {} ".format(price, '.8f'))  

    if mid_currency == 'BNB':
        price = trading_rule_price_BNB(X, price)
    elif mid_currency == 'BTC':   
        price = trading_rule_price_BTC(X, price)
    elif mid_currency == 'ETH':
        price = trading_rule_price_ETH(X, price)
    elif mid_currency == 'USDT':
        price = trading_rule_price_USDT(X, price)

    print("(2) expected PRICE AFTER following the Binance rule : {} ".format(price, '.8f'))

    print("(2) expected AMOUNT BEFORE following the Binance rule : {} ".format(amount_x_from_main, '.8f'))

    if mid_currency == 'BNB':
        amount_x_from_main = trading_rule_amount_BNB(X, amount_x_from_main)
    elif mid_currency == 'BTC':   
        amount_x_from_main = trading_rule_amount_BTC(X, amount_x_from_main)
    elif mid_currency == 'ETH':
        amount_x_from_main = trading_rule_amount_ETH(X, amount_x_from_main)
    elif mid_currency == 'USDT':
        amount_x_from_main = trading_rule_amount_USDT(X, amount_x_from_main)

    print("(2) expected AMOUNT AFTER following the Binance rule : {} ".format(amount_x_from_main, '.8f'))

    amount_mid_from_x = float(amount_x_from_main) * float(price)
    symbol = X + mid_currency
   
    print("(2) selling {} of {} to get {} {}".format(amount_x_from_main, X, amount_mid_from_x, mid_currency))

    order = client().order_limit_sell (
        symbol= symbol,
        quantity= float(amount_x_from_main),
        price= price
    ) 
    # order = client.create_test_order (
    # symbol= symbol[0]+'BTC',
    # side=Client.SIDE_SELL,
    # type=Client.ORDER_TYPE_LIMIT,
    # quantity= amount_x_from_main,
    # timeInForce= "GTC",
    # price= price )

    print("(2) checking if the order is filled or not.... ")

    while True:
        
        existing_order = client().get_order(symbol=symbol, orderId=order['orderId'])

        if( existing_order['status'] == "FILLED" ):
            break
       
        else:
            time.sleep(0.8)
        
    print("(2) FILLED")
 
    transaction_fee = 0

    if X == "BNB" or mid_currency == "BNB":
        transaction_fee = format(float(amount_mid_from_x) * 0.00075, '.8f')
        amount_mid_from_x = float(amount_mid_from_x) * 0.99925
    # else:
    # transaction_fee = format(float(amount_mid_from_x) * 0.001, '.8f')
    # amount_mid_from_x = float(amount_mid_from_x) * 0.999

    print("(2) transaction fee : {} of {} was taken".format( transaction_fee, X ) )
    print("end of job 2")
    lock.release()


def transaction3(mid_currency, main_currency ):

    time.sleep(0.1)

    global lock
    global amount_mid_from_x
    global amount_main_from_mid

    lock.acquire()

    start = time.time()

    price = bidPrice_and_askPrice(mid_currency, main_currency)[0]
    print("(3) expected PRICE BEFORE following the Binance rule : {} ".format(price)) 

    if main_currency == 'BNB':
        price = trading_rule_price_BNB(mid_currency, price)
    elif main_currency == 'BTC':   
        price = trading_rule_price_BTC(mid_currency, price)
    elif main_currency == 'ETH':
        price = trading_rule_price_ETH(mid_currency, price)
    elif main_currency == 'USDT':
        price = trading_rule_price_USDT(mid_currency, price)

    print("(3) expected PRICE AFTER following the Binance rule : {} ".format(price)) 

    amount_main_from_mid = amount_mid_from_x * float(price)
    print("(3) expected AMOUNT BEFORE following the Binance rule : {} ".format(amount_mid_from_x)) 
    
    if main_currency == 'BNB':
        amount_mid_from_x = trading_rule_amount_BNB(mid_currency, amount_mid_from_x)
    elif main_currency == 'BTC':   
        amount_mid_from_x = trading_rule_amount_BTC(mid_currency, amount_mid_from_x)
    elif main_currency == 'ETH':
        amount_mid_from_x = trading_rule_amount_ETH(mid_currency, amount_mid_from_x)
    elif main_currency == 'USDT':
        amount_mid_from_x = trading_rule_amount_USDT(mid_currency, amount_mid_from_x)

    print("(3) expected AMOUNT AFTER following the Binance rule : {} ".format(amount_mid_from_x)) 

    print("(3) get {} of {} from {} of {}".format(amount_main_from_mid, main_currency, amount_mid_from_x, mid_currency))

    symbol = mid_currency + main_currency

    order = client().order_limit_sell (
        symbol= symbol,
        quantity= float(amount_mid_from_x),
        price= price
    ) 
    # order = client.create_test_order (
    # symbol= 'BTCUSDT',
    # side=Client.SIDE_SELL,
    # type=Client.ORDER_TYPE_LIMIT,
    # quantity= amount_mid_from_x,
    # timeInForce= "GTC",
    # price=price )

    print("(3) checking if the order is filled or not.... ")

    while True:
        existing_order = client().get_order(symbol=symbol, orderId=order['orderId'])

        if( existing_order['status'] == "FILLED" ):
            break
    
        else:
            time.sleep(0.8)
        
    print("(3) FILLED")

    # end = time.time()
    # time_elapsed = end-start

    # tickers = client.get_ticker( symbol = 'BTCUSDT' )

    transaction_fee = 0

    if mid_currency == "BNB" or main_currency == "BNB":
        transaction_fee = format(float(amount_mid_from_x) * 0.00075, '.8f')
        amount_mid_from_x = float(amount_mid_from_x) * 0.99925
    # else:
    # transaction_fee = format(float(amount_mid_from_x) * 0.001, '.8f')
    # amount_mid_from_x = float(amount_mid_from_x) * 0.999


    print("(3) transaction fee : {} of {} was taken".format( transaction_fee, mid_currency ) )

    print("end of job 3")
    lock.release()

if __name__ == "__main__":

    print("make_transaction.py")

    