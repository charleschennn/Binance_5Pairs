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
import operator

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

        # get the best 6 pairs of currency
        sorted_d = sorted(global_var.largest_set.items(), key=operator.itemgetter(1), reverse=True)
        sorted_dict = {}
        for i in range(5):
            print(sorted_d[i][0])
            sorted_dict.update({ sorted_d[i][0] : sorted_d[i][1]})

        # print(sorted_d[0][0])
        # print(sorted_d[1][1])
        # print(sorted_d[2])
        # print(sorted_d[3])
        # print(sorted_d[4])
        # print(sorted_d[5])

        # bid_and_ask = bidPrice_and_askPrice(numerator, denominator)
        # bid = bid_and_ask[0]
        # ask = bid_and_ask[1]

        global_var.start_time = datetime.datetime.now()

        now_plus_1 = global_var.start_time + datetime.timedelta(minutes = 1)
        now_plus_8 = global_var.start_time + datetime.timedelta(minutes = 8)
        now_plus_10 = global_var.start_time + datetime.timedelta(minutes = 10)

        # lock = threading.Lock()

        print("Checking the rate condition, make transaction if the most updated rate is profitable.. ")
        
        maximum = max(global_var.largest_set, key=global_var.largest_set.get)
        print(maximum)
        print("Start : {}".format(datetime.datetime.now()))

        while datetime.datetime.now() < now_plus_10:

            if datetime.datetime.now() > now_plus_1 and datetime.datetime.now() < now_plus_8:

                # print("1 Minute : {}".format(datetime.datetime.now()))

                # maximum = max(sorted_dict, key=sorted_dict.get)

                # print("The Largest Pair : {}, 粗利率 : {}".format(maximum, sorted_dict[maximum]))
                # maximum_list = maximum.split("-")

                five_pairs = {}

                # print(sorted_dict)
                for key in sorted_dict:
                    k = key.split("-")
                    numerator = k[0]
                    denominator = k[1]
                    X = k[2]
                    value_temp = float(calculate_profit(X, numerator, denominator)[1])
                    five_pairs.update( { numerator+"-"+denominator+"-"+X : value_temp } )

                maximum = max( five_pairs, key=five_pairs.get )
                value = five_pairs.get(maximum)
                
                # print(maximum)
                # print("value : {}".format(value))

                # real
                if value > 0.003 : 

                # testing purpose
                # if value > 0:

                    maximum_list = maximum.split("-")
                    numerator = maximum_list[0]
                    denominator = maximum_list[1]
                    X = maximum_list[2]

                    print("{} > 0.003, making transaction..".format(value))

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
                    # now_plus_10 = datetime.datetime.now() + datetime.timedelta(minutes = 10)
                    
                    # use denominator currency to buy X
                    # sell X to get numerator
                    # sell numerator to get denominator
                else:
                    time.sleep(1)
                    print("{}  < 0.003, Pair : {}, rechecking the latest rate..".format(value, maximum))
                    continue

            else:

                maximum_list = maximum.split("-")

                numerator = maximum_list[0]
                denominator = maximum_list[1]
                X = maximum_list[2]

                value = float(calculate_profit(X, numerator, denominator)[1])
                # print("The Largest Pair : {}, 粗利率 : {}".format(maximum, value))

                # real
                if value > 0.003 : 

                # testing purpose
                # if value > 0:

                    print("{} > 0.003, making transaction..".format(value))

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
                    # now_plus_1 = global_var.start_time + datetime.timedelta(minutes = 1)
                    # now_plus_8 = global_var.start_time + datetime.timedelta(minutes = 8)
                    # now_plus_10 = datetime.datetime.now() + datetime.timedelta(minutes = 10)
                    
                    # use denominator currency to buy X
                    # sell X to get numerator
                    # sell numerator to get denominator
                else:
                    time.sleep(1)
                    print("{}  < 0.003, Pair : {}-{}-{}, rechecking the latest rate..".format(value, numerator, denominator, X))
                    continue
    
        
        print("No transaction was made in the last 10 minutes, recheck the new currency pair now..")
        print(datetime.datetime.now())

        # keep checking the rate condition periodically for 10 minutes 
        # until it satisfy the requirement and make the transaction. 
        # When the 10 minutes limit has exceeded, recheck the new currency pair
        


