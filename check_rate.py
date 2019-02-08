from Utilities import calculate_profit
import time
import threading
import global_var

def ETH_USDT():
    
    # global global_var.largest_set

    start_time = time.time()

    ETH_USDT_currency_tuple = 'IOTA', 'NULS', 'WAVES', 'LTC', 'ICX', 'TUSD', 'ETC', 'QTUM', 'ADA', 'VET', 'XRP', 'BNB', 'EOS', 'XLM', 'TRX', 'LINK', 'ONT', 'NEO'
    
    # largest_ETH_USDT = -100
    # largest_ETH_USDT_key = None

    for i in ETH_USDT_currency_tuple:
        result = calculate_profit(i, "ETH", "USDT")
        # if float(result[1]) > largest_ETH_USDT:
        #     largest_ETH_USDT = float(result[1])
        largest_ETH_USDT_key = "ETH-USDT-"+result[0]
        
        temp = { largest_ETH_USDT_key : float(result[1])}
        global_var.largest_set.update(temp)
        

    # print("{} : {}%".format(largest_ETH_USDT_key, largest_ETH_USDT))
    end_time = time.time()
    time_duration = end_time - start_time
    print("{} seconds is used".format(time_duration))

def BNB_BTC():

    # global global_var.largest_set

    BNB_BTC_currency_tuple = 'ICX', 'STEEM', 'XRP', 'WABI', 'NAV', 'ADX', 'DLT', 'TUSD', 'THETA', 'NEO', 'CVC', 'REP', 'RVN', 'NANO', 'NXS', 'LOOM', 'REN', 'ENJ', 'ETC', 'MFT', 'WAVES', 'LTC', 'APPC', 'BCPT', 'BAT', 'AMB', 'SKY', 'WTC', 'ZIL', 'TRX', 'WAN', 'BRD', 'VIA', 'VET', 'MITH', 'MCO', 'IOTA', 'AE', 'DCR', 'OST', 'ZEN', 'POLY', 'PHX', 'BLZ', 'RDN', 'NULS', 'QLC', 'GO', 'NEBL', 'PIVX', 'GTO', 'POA', 'GNT', 'EOS', 'POWR', 'AION', 'ONT', 'RCN', 'XLM', 'XEM', 'CND', 'STORM', 'ARDR', 'BTS', 'YOYO', 'QTUM', 'NCASH', 'BTT', 'QSP', 'NAS', 'LSK', 'XZC', 'ADA', 'CMT', 'SYS', 'RLC', 'AGI', 'SC'
    
    start_time = time.time()

    # largest_BNB_BTC = -100
    # largest_BNB_BTC_key = None

    for i in BNB_BTC_currency_tuple:
        result = calculate_profit(i, "BNB", "BTC")
        # if float(result[1]) > largest_BNB_BTC:
        #     largest_BNB_BTC = float(result[1])
        largest_BNB_BTC_key = "BNB-BTC-"+result[0]
            
        temp = { largest_BNB_BTC_key : float(result[1])}
        global_var.largest_set.update(temp)

    # print("{} : {}%".format(largest_BNB_BTC_key, largest_BNB_BTC))
    end_time = time.time()
    time_duration = end_time - start_time
    print("{} seconds is used".format(time_duration))

def BNB_ETH():

    # global global_var.largest_set

    BNB_ETH_currency_tuple = 'RCN', 'IOTA', 'NEBL', 'OST', 'NEO', 'MFT', 'PHX', 'POWR', 'YOYO', 'NXS', 'NANO', 'GNT', 'VET', 'STEEM', 'RDN', 'AE', 'BAT', 'VIA', 'ARDR', 'SC', 'GTO', 'TUSD', 'CMT', 'XRP', 'MCO', 'RLC', 'ICX', 'XZC', 'BRD', 'XLM', 'NCASH', 'DLT', 'NULS', 'THETA', 'QSP', 'NAS', 'CND', 'ZIL', 'SKY', 'CVC', 'WAVES', 'PIVX', 'AGI', 'ADA', 'ONT', 'STORM', 'TRX', 'AMB', 'APPC', 'EOS', 'POA', 'ADX', 'ZEN', 'ETC', 'REP', 'LTC', 'XEM', 'WABI', 'LOOM', 'AION', 'BCPT', 'BTS', 'WAN', 'BLZ', 'LSK', 'SYS', 'ENJ', 'QTUM', 'NAV', 'QLC', 'WTC'
    
    start_time = time.time()

    # largest_BNB_ETH = -100
    # largest_BNB_ETH_key = None

    for i in BNB_ETH_currency_tuple:
        result = calculate_profit(i, "BNB", "ETH")
        # if float(result[1]) > largest_BNB_ETH:
        #     largest_BNB_ETH = float(result[1])
        largest_BNB_ETH_key = "BNB-ETH-"+result[0]

        temp = { largest_BNB_ETH_key : float(result[1])}
        global_var.largest_set.update(temp)

    # print("{} : {}%".format(largest_BNB_ETH_key, largest_BNB_ETH))
    end_time = time.time()
    time_duration = end_time - start_time 
    print("{} seconds is used".format(time_duration))


def BNB_USDT():

    # global global_var.largest_set

    start_time = time.time()

    BNB_USDT_currency_tuple = 'BTT', 'LTC', 'IOTA', 'TRX', 'VET', 'ICX', 'QTUM', 'NEO', 'EOS', 'NULS', 'XLM', 'ONT', 'TUSD', 'ETC', 'ADA', 'WAVES', 'XRP'

    # largest_BNB_USDT = -100
    # largest_BNB_USDT_key = None

    for i in BNB_USDT_currency_tuple:
        result = calculate_profit(i, "BNB", "USDT")
        # if float(result[1]) > largest_BNB_USDT:
        #     largest_BNB_USDT = float(result[1])
        largest_BNB_USDT_key = "BNB-USDT-"+result[0]

        temp = { largest_BNB_USDT_key : float(result[1])}
        global_var.largest_set.update(temp)

    # print("{} : {}%".format(largest_BNB_USDT_key, largest_BNB_USDT))
    end_time = time.time()
    time_duration = end_time - start_time
    print("{} seconds is used".format(time_duration))

def BTC_USDT():

    # global global_var.largest_set

    BTC_USDT_currency_tuple = 'LTC', 'ETH', 'ETC', 'QTUM', 'BCHABC', 'TUSD', 'LINK', 'ADA', 'ONT', 'VET', 'TRX', 'ICX', 'BCHSV', 'EOS', 'XRP', 'BTT', 'NULS', 'NEO', 'XLM', 'WAVES', 'IOTA'

    start_time = time.time()

    # largest_BTC_USDT = -100
    # largest_BTC_USDT_key = None

    for i in BTC_USDT_currency_tuple:
        result = calculate_profit(i, "BTC", "USDT")
        # if float(result[1]) > largest_BTC_USDT:
        #     largest_BTC_USDT = float(result[1])
        largest_BTC_USDT_key = "BTC-USDT-"+result[0]

        temp = { largest_BTC_USDT_key : float(result[1])}
        global_var.largest_set.update(temp)

    # print("{} : {}%".format(largest_BTC_USDT_key, largest_BTC_USDT))
    end_time = time.time()
    time_duration = end_time - start_time
    print("{} seconds is used".format(time_duration))


def ETH_BTC():

    # global global_var.largest_set

    ETH_BTC_currency_tuple = 'OST', 'NANO', 'EDO', 'AMB', 'XZC', 'POA', 'GVT', 'GXS', 'BCPT', 'FUEL', 'POE', 'WAN', 'LTC', 'KNC', 'BNT', 'MDA', 'LINK', 'NEO', 'BTG', 'AION', 'ELF', 'CLOAK', 'DNT', 'IOTX', 'HOT', 'GTO', 'ONT', 'WINGS', 'DENT', 'OMG', 'ETC', 'XEM', 'QTUM', 'VIBE', 'TRX', 'XVG', 'SALT', 'MTH', 'DLT', 'YOYO', 'QSP', 'BRD', 'MFT', 'ADA', 'IOST', 'VET', 'NEBL', 'POWR', 'CDT', 'ARN', 'BTS', 'LUN', 'SNT', 'VIB', 'WABI', 'STORJ', 'QLC', 'STEEM', 'VIA', 'NPXS', 'LOOM', 'REP', 'DASH', 'NULS', 'NCASH', 'NXS', 'EOS', 'RDN', 'ARK', 'AST', 'TNT', 'ENJ', 'SC', 'MTL', 'IOTA', 'KMD', 'ARDR', 'ICX', 'CVC', 'XRP', 'INS', 'SNGLS', 'XMR', 'PPT', 'STORM', 'BCD', 'ENG', 'CND', 'BLZ', 'ZEN', 'TNB', 'PHX', 'ADX', 'ZIL', 'KEY', 'DOCK', 'LEND', 'LRC', 'SKY', 'THETA', 'PIVX', 'WAVES', 'GNT', 'APPC', 'MANA', 'BAT', 'WPR', 'EVX', 'RCN', 'STRAT', 'REQ', 'MCO', 'CMT', 'GRS', 'NAV', 'BQX', 'FUN', 'DGD', 'LSK', 'NAS', 'OAX', 'AE', 'MOD', 'HC', 'SNM', 'BNB', 'AGI', 'TUSD', 'RLC', 'DATA', 'SUB', 'XLM', 'ZRX', 'QKC', 'ZEC', 'WTC', 'SYS'

    start_time = time.time()

    # largest_ETH_BTC = -100
    # largest_ETH_BTC_key = None

    for i in ETH_BTC_currency_tuple:
        result = calculate_profit(i, "ETH", "BTC")
        # if float(result[1]) > largest_ETH_BTC:
        #     largest_ETH_BTC = float(result[1])
        largest_ETH_BTC_key = "ETH-BTC-"+result[0]
    
        temp = { largest_ETH_BTC_key : float(result[1])}
        global_var.largest_set.update(temp)
    
    # print("{} : {}%".format(largest_ETH_BTC_key, largest_ETH_BTC))
    end_time = time.time()
    time_duration = end_time - start_time
    print("{} seconds is used".format(time_duration))


if __name__ == "__main__":


    print("check_rate.py")

    # start_time = time.time()

    # largest_set = {}
    # # total_currency_cnt = len(ETH_USDT_currency_tuple) + len(BNB_BTC_currency_tuple) + len(BNB_ETH_currency_tuple) + len(BNB_USDT_currency_tuple) + len(BTC_USDT_currency_tuple) + len(ETH_BTC_currency_tuple)

    # t1=threading.Thread(target=ETH_USDT)
    # t2=threading.Thread(target=BNB_BTC)
    # t3=threading.Thread(target=BNB_ETH)
    # t4=threading.Thread(target=BNB_USDT)
    # t5=threading.Thread(target=BTC_USDT)
    # t6=threading.Thread(target=ETH_BTC)

    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    # t6.start()
    
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()

    # print(largest_set)

    # maximum = max(largest_set, key=largest_set.get)
    # print(maximum, largest_set[maximum])
    # end_time = time.time()
    # time_duration = end_time - start_time
    # print("{} seconds is used".format(time_duration))