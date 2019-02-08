from Utilities import calculate_profit
from Utilities import bidPrice_and_askPrice
from Utilities import set_initial_cost
from Utilities import initialize_api as client
import check_rate
import time
import datetime
import threading
import global_var
import make_transaction


if __name__ == "__main__":

    
    while True:

        global_var.largest_set = {}

        t1=threading.Thread(target=check_rate.ETH_USDT)
        t2=threading.Thread(target=check_rate.BNB_BTC)
        t3=threading.Thread(target=check_rate.BNB_ETH)
        t4=threading.Thread(target=check_rate.BNB_USDT)
        t5=threading.Thread(target=check_rate.BTC_USDT)
        t6=threading.Thread(target=check_rate.ETH_BTC)

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()

        maximum = max(global_var.largest_set, key=global_var.largest_set.get)
        print("The Largest Pair : {}, 粗利率 : {}".format(maximum, global_var.largest_set[maximum]))
        maximum = maximum.split("-")

        numerator = maximum[0]
        denominator = maximum[1]
        X = maximum[2]

        # bid_and_ask = bidPrice_and_askPrice(numerator, denominator)
        # bid = bid_and_ask[0]
        # ask = bid_and_ask[1]

        global_var.start_time = datetime.datetime.now()

        now_plus_10 = global_var.start_time + datetime.timedelta(minutes = 10)
        # lock = threading.Lock()

        print("Checking the rate condition, make transaction if the most updated rate is profitable.. ")
        print(datetime.datetime.now())

        while datetime.datetime.now() < now_plus_10:

            value = float(calculate_profit(X, numerator, denominator)[1])
            # real
            if value > 0.0035 : 

            # testing purpose
            # if value > 0:

                print("{} > 0.0035, making transaction..".format(value))

                initial_cost = set_initial_cost(True, X, numerator, denominator)

                transaction1=threading.Thread(target=make_transaction.transaction1(initial_cost, X, denominator ))
                transaction1.start()
                transaction1.join()

                transaction2=threading.Thread(target=make_transaction.transaction2(X, numerator ))
                transaction2.start()
                transaction2.join()

                transaction3=threading.Thread(target=make_transaction.transaction3(numerator, denominator ))
                transaction3.start()
                transaction3.join()

                # transaction were made, reset the timer and keep checking the same pair until the 10 minutes requirement is passed again
                now_plus_10 = datetime.datetime.now() + datetime.timedelta(minutes = 10)
                
                # use denominator currency to buy X
                # sell X to get numerator
                # sell numerator to get denominator
            else:
                time.sleep(1)
                print("{}  < 0.0035 , recheck the latest rate of {}-{}-{} pair to check the profit..".format(value, numerator, denominator, X))
                continue
        
        print("10 minutes has passed and no transaction was been made, recheck the new currency pair now ")
        print(datetime.datetime.now())

        # keep checking the rate condition periodically for 10 minutes 
        # until it satisfy the requirement and make the transaction. 
        # When the 10 minutes limit has exceeded, recheck the new currency pair
        


