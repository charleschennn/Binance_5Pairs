from binance.client import Client
import csv
import datetime
import time
import requests
import math

def initialize_api():

    api_key = "WZmOKyyiNsxDMmxpRfS1ZVR9nWxvTsmSuxdEQrn6BGNGxbKaDJCCQOLs63jWq3zp"
    api_secret = "SzoN52Aj51aLVGWkPItqp8P0lNSzzVtkkMTxxxYA5x9HVxQ3sAmrSgDZ0pOBLGUK"  
    client = Client( api_key, api_secret )
    return client


def bidPrice_and_askPrice(numerator, denominator):

    url = "https://api.binance.com/api/v3/ticker/bookTicker?symbol="

    symbol = numerator + denominator
    # ticker = client.get_orderbook_ticker( symbol = symbol )
    ticker = url + symbol
    r = requests.get(ticker)
    result = r.json()

    # bidPrice = result.get('bidPrice')
    # bidQty = result.get('bidQty')
    # askPrice = result.get('askPrice')
    # askQty = result.get('askQty')
    
    # # return result.get('bidPrice')+","+ ticker.get('askPrice')+","
    return (result.get('bidPrice'), result.get('askPrice'), result.get('bidQty'), result.get('askQty'))

    # client = initialize_api()
    # symbol = numerator + denominator
    # ticker = client.get_orderbook_ticker( symbol = symbol )

    # return ( ticker.get('bidPrice'), ticker.get('askPrice'), ticker.get('bidQty'), ticker.get('askQty') )


def calculate_profit(X, mid_currency, main_currency):

    X_to_main = bidPrice_and_askPrice(X, main_currency)

    X_to_mid = bidPrice_and_askPrice(X, mid_currency)

    mid_to_main = bidPrice_and_askPrice(mid_currency, main_currency)

    D = float(X_to_main[1])
    F = float(X_to_mid[0])
    J = float(mid_to_main[0])

    B = float(X_to_main[0])
    H = float(X_to_mid[1])
    L = float(mid_to_main[1])

    formula1 = ( 1 / D * F * J ) - 1
    # buy sell sell

    formula2 = ( ( ( 1 / L) / H ) * B ) - 1
    # sell buy buy

    return (X, formula1)

    # C = float(X_to_main[0])
    # D = float(X_to_main[1])
    # E = float(X_to_mid[0])
    # F = float(X_to_mid[1])
    # G = float(mid_to_main[0])
    # H = float(mid_to_main[1])

    # if mid_currency == 'BTC' and main_currency == 'USDT':
    #     print(" BTC / USDT (売り成行): {}".format(H))
    #     print(" {} / USDT (売り成行): {}".format(X, D))
    #     print(" {} / BTC (買い成行): {}".format(X, E))
    #     print(" =============== ")


    # formula1 = ((H / D) * E * H - H) / H
    # formula2 = ((1 / F) * C - H) / G
    


def generate_csv( numerator, denominator, largest_value_and_key ):

    filename = "report_"+numerator+"_"+denominator+"_X_0205.csv"

    with open(filename,'a') as f:

        writer = csv.writer(f)

        while True:

            # JP_time_local = datetime.datetime.now()
            JP_time_AWS = datetime.datetime.now() + datetime.timedelta(hours=9)

            formatted_time =  JP_time_AWS.strftime("%H:%M:%S")
            # print("{}_{}_X : {} ".format(numerator, denominator, formatted_time))

            pair = numerator + " - " + denominator + " - " + largest_value_and_key[0]

            value = str(largest_value_and_key[1])

            row = formatted_time+", "+pair+", "+value+" %"
    
            writer.writerow([row]) 

            print("done")

            time.sleep(60)

def trading_rule_price_ETH(symbol, returned_price):

    returned_price = float(returned_price)

    if ( symbol == 'QKC' or symbol == 'ZRX' or symbol == 'SUB' or symbol == 'DATA' or symbol == 'SNM' or symbol == 'FUN' or symbol == 'GRS' or symbol == 'REQ' or symbol == 'WPR' or symbol == 'MANA' or symbol == 'LRC' or symbol == 'LEND' or symbol == 'DOCK' or symbol == 'KEY' or symbol == 'TNB' or symbol == 'SNGLS' or symbol == 'TNT' or symbol == 'NPXS' or symbol == 'VIB' or symbol == 'SNT' or symbol == 'ARN' or symbol == 'CDT' or symbol == 'IOST' or symbol == 'MTH' or symbol == 'XVG' or symbol == 'DENT' or symbol == 'HOT' or symbol == 'IOTX' or symbol == 'DNT' or symbol == 'ELF' or symbol == 'POE' or symbol == 'FUEL' or symbol == 'QLC' or symbol == 'ENJ' or symbol == 'IOTA' or symbol == 'SYS' or symbol == 'BLZ' or symbol == 'BTS' or symbol == 'BCPT' or symbol == 'LOOM' or symbol == 'WABI' or symbol == 'XEM' or symbol == 'POA' or symbol == 'AMB' or symbol == 'STORM' or symbol == 'AGI' or symbol == 'CVC' or symbol == 'ZIL' or symbol == 'CND' or symbol == 'QSP' or symbol == 'THETA' or symbol == 'DLT' or symbol == 'NCASH' or symbol == 'CMT' or symbol == 'GTO' or symbol == 'SC' or symbol == 'ARDR' or symbol == 'BAT' or symbol == 'GNT' or symbol == 'YOYO' or symbol == 'POWR' or symbol == 'PHX' or symbol == 'MFT' or symbol == 'OST' or symbol == 'RCN' or symbol == 'LINK' or symbol == 'TRX' or symbol == 'XLM' or symbol == 'XRP' or symbol == 'VET' or symbol == 'ADA' or symbol == 'TUSD' or symbol == 'NULS' or symbol == 'IOTA' ):
        returned_price = math.floor(returned_price * 100000000 ) / 100000000
        returned_price = format(returned_price, '.8f')
    elif( symbol == 'OAX' or symbol == 'BQX' or symbol == 'EVX' or symbol == 'QKC' or symbol == 'ENG' or symbol == 'STORJ' or symbol == 'VIBE' or symbol == 'WINGS' or symbol == 'MDA' or symbol == 'KNC' or symbol == 'ADX' or symbol == 'APPC' or  symbol == 'BRD' or symbol == 'RDN' ):
        returned_price = math.floor(returned_price * 10000000 ) / 10000000
        returned_price = format(returned_price, '.7f')
    elif ( symbol == 'HC' or symbol == 'MOD' or symbol == 'LSK' or symbol == 'STRAT' or symbol == 'PPT' or symbol == 'INS' or symbol == 'KMD' or symbol == 'MTL' or symbol == 'ARK' or symbol == 'NXS' or symbol == 'LUN' or symbol == 'SALT' or symbol == 'OMG' or symbol == 'CLOAK' or symbol == 'BTG' or symbol == 'BNT' or symbol == 'WAN' or symbol == 'GXS' or symbol == 'GVT' or symbol == 'EDO' or symbol == 'WTC' or symbol == 'NAV' or symbol == 'LSK' or symbol == 'AION' or symbol == 'PIVX' or symbol == 'NAS' or symbol == 'XZC' or symbol == 'ICX' or symbol == 'RLC' or symbol == 'MCO' or symbol == 'VIA' or symbol == 'AE' or symbol == 'STEEM' or symbol == 'NANO' or symbol == 'NEBL' or symbol == 'NEO' or symbol == 'ONT' or symbol == 'EOS' or symbol == 'BNB' or symbol == 'QTUM' or symbol == 'ETC' or symbol == 'ICX' or symbol == 'WAVES' ):
        returned_price = math.floor(returned_price * 1000000 ) / 1000000
        returned_price = format(returned_price, '.6f')
    elif ( symbol == 'ZEC' or symbol == 'DGD' or symbol == 'BCD' or symbol == 'XMR' or symbol == 'DASH' or symbol == 'REP' or symbol == 'ZEN' or symbol == 'SKY' or symbol == 'LTC' ):
        returned_price = math.floor(returned_price * 100000 ) / 100000
        returned_price = format(returned_price, '.5f')

    return returned_price

def trading_rule_amount_ETH(symbol, returned_amount):

    returned_amount = float(returned_amount)

    if ( symbol == 'QKC' or symbol == 'ZRX' or symbol == 'SUB' or symbol == 'DATA' or symbol == 'SNM' or symbol == 'OAX' or symbol == 'FUN' or symbol == 'BQX' or symbol == 'GRS' or symbol == 'REQ' or symbol == 'EVX' or symbol == 'WPR' or symbol == 'MANA' or symbol == 'LRC' or symbol == 'LEND' or symbol == 'DOCK' or symbol == 'KEY' or symbol == 'TNB' or symbol == 'ENG' or symbol == 'SNGLS' or symbol == 'TNT' or symbol == 'AST' or symbol == 'NPXS' or symbol == 'STORJ' or symbol == 'VIB' or symbol == 'SNT' or symbol == 'ARN' or symbol == 'CDT' or symbol == 'IOST' or symbol == 'MTH' or symbol == 'XVG' or symbol == 'VIBE' or symbol == 'DENT' or symbol == 'WINGS' or symbol == 'HOT' or symbol == 'IOTX' or symbol == 'DNT' or symbol == 'ELF' or symbol == 'MDA' or symbol == 'KNC' or symbol == 'POE' or symbol == 'FUEL' or symbol == 'QLC' or symbol == 'ENJ' or symbol == 'SYS' or symbol == 'BLZ' or symbol == 'BTS' or symbol == 'BCPT' or symbol == 'LOOM' or symbol == 'WABI' or symbol == 'XEM' or symbol == 'ADX' or symbol == 'POA' or symbol == 'APPC' or symbol == 'AMB' or symbol == 'STORM' or symbol == 'AGI' or symbol == 'CVC' or symbol == 'ZIL' or symbol == 'CND' or symbol == 'QSP' or symbol == 'THETA' or symbol == 'DLT' or symbol == 'NCASH' or symbol == 'BRD' or symbol == 'CMT' or symbol == 'GTO' or symbol == 'SC' or symbol == 'ARDR' or symbol == 'BAT' or symbol == 'RDN' or symbol == 'GNT' or symbol == 'YOYO' or symbol == 'POWR' or symbol == 'PHX' or symbol == 'MFT' or symbol == 'OST' or symbol == 'RCN' or symbol == 'LINK' or symbol == 'TRX' or symbol == 'XLM' or symbol == 'XRP' or symbol == 'VET' or symbol == 'ADA' or symbol == 'TUSD' or symbol == 'NULS' or symbol == 'IOTA'):
        returned_amount =  math.floor(returned_amount )
    elif ( symbol == 'HC' or symbol == 'MOD' or symbol == 'LSK' or symbol == 'STRAT' or symbol == 'PPT' or symbol == 'INS' or symbol == 'KMD' or symbol == 'MTL' or symbol == 'ARK' or symbol == 'NXS' or symbol == 'LUN' or symbol == 'SALT' or symbol == 'OMG' or symbol == 'CLOAK' or symbol == 'BTG' or symbol == 'BNT' or symbol == 'WAN' or symbol == 'GXS' or symbol == 'GVT' or symbol == 'EDO' or symbol == 'WTC' or symbol == 'NAV' or symbol == 'LSK' or symbol == 'AION' or symbol == 'PIVX' or symbol == 'NAS' or symbol == 'XZC' or symbol == 'ICX' or symbol == 'RLC' or symbol == 'MCO' or symbol == 'VIA' or symbol == 'AE' or symbol == 'STEEM' or symbol == 'NANO' or symbol == 'NXS' or symbol == 'NEBL' or symbol == 'NEO' or symbol == 'ONT' or symbol == 'EOS' or symbol == 'BNB' or symbol == 'QTUM' or symbol == 'ETC' or symbol == 'ICX' or symbol == 'WAVES' ):
        returned_amount =  math.floor(returned_amount * 100 ) / 100
        returned_amount = format(returned_amount, '.2f')
    elif ( symbol == 'ZEC' or symbol == 'DGD' or symbol == 'BCD' or symbol == 'XMR' or symbol == 'REP' or symbol == 'ZEN' or symbol == 'SKY' or symbol == 'LTC' ):
        returned_amount =  math.floor(returned_amount * 1000 ) / 1000
        returned_amount = format(returned_amount, '.3f')

    return returned_amount

def trading_rule_price_BNB(symbol, returned_price):

    returned_price = float(returned_price)

    if ( symbol == 'BTT' ):
        returned_price = math.floor(returned_price * 100000000 ) / 100000000
        returned_price = format(returned_price, '.8f')
    elif ( symbol == 'GO' or symbol == 'RVN' or symbol == 'QLC' or symbol == 'ENJ' or symbol == 'TRX' or symbol == 'STORM' or symbol == 'ZIL' or symbol == 'CND' or symbol == 'QSP' or symbol == 'NCASH' or symbol == 'SC' or symbol == 'YOYO' or symbol == 'PHX' or symbol == 'MFT' or symbol == 'OST' or symbol == 'RCN' or symbol == 'TRX' ):
        returned_price = math.floor(returned_price * 1000000 ) / 1000000
        returned_price = format(returned_price, '.6f')
    elif ( symbol == 'POLY' or symbol == 'MITH' or symbol == 'NAV' or symbol == 'SYS' or symbol == 'BLZ' or symbol == 'WAN' or symbol == 'BTS' or symbol == 'BCPT' or symbol == 'AION' or symbol == 'LOOM' or symbol == 'WABI' or symbol == 'XEM' or symbol == 'ADX' or symbol == 'POA' or symbol == 'APPC' or symbol == 'AGI' or symbol == 'PIVX' or symbol == 'CVC' or symbol == 'NAS' or symbol == 'THETA' or symbol == 'DLT' or symbol == 'BRD' or symbol == 'RLC' or symbol == 'MCO' or symbol == 'CMT' or symbol == 'GTO' or symbol == 'ARDR' or symbol == 'VIA' or symbol == 'BAT' or symbol == 'AE' or symbol == 'RDN' or symbol == 'STEEM' or symbol == 'GNT' or symbol == 'POWR' or symbol == 'NEBL' or symbol == 'IOTA' or symbol == 'XRP' or symbol == 'ADA' or symbol == 'TUSD' or symbol == 'ONT' or symbol == 'XLM' or symbol == 'NULS' or symbol == 'QTUM' or symbol == 'ICX' or symbol == 'VET' or symbol == 'IOTA' ):
        returned_price = math.floor(returned_price * 100000 ) / 100000
        returned_price = format(returned_price, '.5f')
    elif ( symbol == 'NXS' or symbol == 'WTC' or symbol == 'LSK' or symbol == 'NANO' or symbol == 'WAVES' or symbol == 'ETC' or symbol == 'EOS' ):
        returned_price = math.floor(returned_price * 10000 ) / 10000
        returned_price = format(returned_price, '.4f')
    elif ( symbol == 'DCR' or symbol == 'REP' or symbol == 'ZEN' or symbol == 'SKY' or symbol == 'XZC' or symbol == 'NEO' ):
        returned_price = math.floor(returned_price * 1000 ) / 1000
        returned_price = format(returned_price, '.3f')
    elif ( symbol == 'LTC' ):
        returned_price = math.floor(returned_price * 100 ) / 100
        returned_price = format(returned_price, '.2f')

    return returned_price

def trading_rule_amount_BNB(symbol, returned_amount):

    returned_amount = float(returned_amount)

    if ( symbol == 'GO' or symbol == 'RVN' or symbol == 'QLC' or symbol == 'ENJ' or symbol == 'TRX' or symbol == 'STORM' or symbol == 'ZIL' or symbol == 'QSP' or symbol == 'NCASH' or symbol == 'SC' or symbol == 'YOYO' or symbol == 'PHX' or symbol == 'MFT' or symbol == 'OST' or symbol == 'RCN' or symbol == 'TRX' or symbol == 'BTT' ):
        returned_amount =  math.floor(returned_amount )
    elif ( symbol == 'POLY' or symbol == 'MITH' or symbol == 'REN' or symbol == 'ICX' or symbol == 'NAV' or symbol == 'SYS' or symbol == 'BLZ' or symbol == 'WAN' or symbol == 'BTS' or symbol == 'BCPT' or symbol == 'AION' or symbol == 'LOOM' or symbol == 'WABI' or symbol == 'XEM' or symbol == 'ADX' or symbol == 'POA' or symbol == 'APPC' or symbol == 'AMB' or symbol == 'AGI' or symbol == 'PIVX' or symbol == 'NAS' or symbol == 'THETA' or symbol == 'DLT' or symbol == 'BRD' or symbol == 'RLC' or symbol == 'MCO' or symbol == 'CMT' or symbol == 'GTO' or symbol == 'ARDR' or symbol == 'VIA' or symbol == 'BAT' or symbol == 'AE' or symbol == 'RDN' or symbol == 'STEEM' or symbol == 'GNT' or symbol == 'POWR' or symbol == 'NEBL' or symbol == 'XRP' or symbol == 'ADA' or symbol == 'TUSD' or symbol == 'ONT' or symbol == 'XLM' or symbol == 'NULS' or symbol == 'QTUM' or symbol == 'ICX' or symbol == 'VET' or symbol == 'IOTA' ):
        returned_amount =  math.floor(returned_amount * 10 ) / 10
        returned_amount = format(returned_amount, '.1f')
    elif ( symbol == 'WTC' or symbol == 'LSK' or symbol == 'NANO' or symbol == 'NXS' or symbol == 'WAVES' or symbol == 'ETC' or symbol == 'EOS' ):
        returned_amount =  math.floor(returned_amount * 100 ) / 100
        returned_amount = format(returned_amount, '.2f')
    elif ( symbol == 'AAA' or symbol == 'DCR' or symbol == 'REP' or symbol == 'ZEN' or symbol == 'SKY' or symbol == 'XZC' or symbol == 'NEO' ):
        returned_amount =  math.floor(returned_amount * 1000 ) / 1000
        returned_amount = format(returned_amount, '.3f')
    elif ( symbol == 'LTC' ):
        returned_amount =  math.floor(returned_amount * 100000 ) / 100000
        returned_amount = format(returned_amount, '.5f')

    return returned_amount


def trading_rule_price_USDT( symbol, returned_price ):

    returned_price = float(returned_price)

    if ( symbol == 'BTT' ):
        returned_price = math.floor(returned_price * 10000000 ) / 10000000
        returned_price = format(returned_price, '.7f')
    elif ( symbol == 'VET' ):
        returned_price = math.floor(returned_price * 1000000 ) / 1000000
        returned_price = format(returned_price, '.6f')
    elif ( symbol == 'ADA' or symbol == 'TRX' or symbol == 'XLM' or symbol == 'XRP'):
        returned_price = math.floor(returned_price * 100000 ) / 100000
        returned_price = format(returned_price, '.5f')
    elif ( symbol == 'IOTA' or symbol == 'WAVES' or symbol == 'IOTA' or symbol == 'NULS' or symbol == 'TUSD' or symbol == 'BNB' or symbol == 'EOS' or symbol == 'ICX' or symbol == 'ETC' or symbol == 'ONT' ):
        returned_price = math.ceil(returned_price * 10000 ) / 10000
        returned_price = format(returned_price, '.4f')        
    elif ( symbol == 'NEO' or symbol == 'QTUM' ):
        returned_price = math.ceil(returned_price * 1000 ) / 1000
        returned_price = format(returned_price, '.3f')
    elif ( symbol == 'BCHABC' or symbol == 'BCHSV' or symbol == 'ETH' or symbol == 'LTC' ):
        returned_price = math.ceil(returned_price * 100 ) / 100
        returned_price = format(returned_price, '.2f')

    return returned_price

def trading_rule_amount_USDT(symbol, returned_amount):

    returned_amount = float(returned_amount)

    if( symbol == 'BTT' or symbol == 'VET'):
        returned_amount =  math.floor(returned_amount )
    elif ( symbol == 'ADA' or symbol == 'TRX' or symbol == 'XLM' or symbol == 'XRP' ):
        returned_amount =  math.floor(returned_amount * 10 ) / 10
        returned_amount = format(returned_amount, '.1f')
    elif ( symbol == 'LINK' or symbol == 'WAVES' or symbol == 'IOTA' or symbol == 'ONT' or symbol == 'NULS' or symbol == 'TUSD' or symbol == 'BNB' or symbol == 'EOS' or symbol == 'ICX' or symbol == 'ETC' ):
        returned_amount =  math.floor(returned_amount * 100 ) / 100
        returned_amount = format(returned_amount, '.2f')
    elif ( symbol == 'NEO' or symbol == 'QTUM' ):
        returned_amount =  math.floor(returned_amount * 1000 ) / 1000
        returned_amount = format(returned_amount, '.3f')
    elif ( symbol == 'BCHABC' or symbol == 'BCHSV' or symbol == 'ETH' or symbol == 'LTC' ):
        returned_amount =  math.floor(returned_amount * 100000 ) / 100000
        returned_amount = format(returned_amount, '.5f')

    return returned_amount


def trading_rule_price_BTC(symbol, returned_price):

    returned_price = float(returned_price)

    if ( symbol == 'QKC' or symbol == 'ZRX' or symbol == 'SUB' or symbol == 'DATA' or symbol == 'SNM' or symbol == 'OAX' or symbol == 'FUN' or symbol == 'BQX' or symbol == 'GRS' or symbol == 'REQ' or symbol == 'EVX' or symbol == 'WPR' or symbol == 'MANA' or symbol == 'LRC' or symbol == 'LEND' or symbol == 'DOCK' or symbol == 'KEY' or symbol == 'TNB' or symbol == 'ENG' or symbol == 'SNGLS' or symbol == 'TNT' or symbol == 'AST' or symbol == 'NPXS' or symbol == 'STORJ' or symbol == 'VIB' or symbol == 'SNT' or symbol == 'ARN' or symbol == 'CDT' or symbol == 'IOST' or symbol == 'QSP' or symbol == 'MTH' or symbol == 'XVG' or symbol == 'VIBE' or symbol == 'DENT' or symbol == 'WINGS' or symbol == 'HOT' or symbol == 'IOTX' or symbol == 'DNT' or symbol == 'ELF' or symbol == 'LINK' or symbol == 'MDA' or symbol == 'BNT' or symbol == 'KNC' or symbol == 'POE' or symbol == 'FUEL' or symbol == 'AMB' or symbol == 'SC' or symbol == 'AGI' or symbol == 'SYS' or symbol == 'CMT' or symbol == 'BTT' or symbol == 'NCASH' or symbol == 'YOYO' or symbol == 'BTS' or symbol == 'ARDR' or symbol == 'STORM' or symbol == 'CND' or symbol == 'XEM' or symbol == 'XLM' or symbol == 'RCN' or symbol == 'POWR' or symbol == 'GNT' or symbol == 'POA' or symbol == 'GTO' or symbol == 'GO' or symbol == 'QLC' or symbol == 'RDN' or symbol == 'BLZ' or symbol == 'PHX' or symbol == 'POLY' or symbol == 'OST' or symbol == 'MITH' or symbol == 'BRD' or symbol == 'TRX' or symbol == 'ZIL' or symbol == 'AMB' or symbol == 'BAT' or symbol == 'BCPT' or symbol == 'APPC' or symbol == 'MFT' or symbol == 'ENJ' or symbol == 'REN' or symbol == 'LOOM' or  symbol == 'RVN' or symbol == 'CVC' or symbol == 'THETA' or symbol == 'DLT' or symbol == 'ADX' or  symbol == 'WABI' or symbol == 'ADA' or symbol == 'TRX' or symbol == 'VET' or symbol == 'XLM' or symbol == 'XRP' or  symbol == 'IOTA' or symbol == 'NULS' or symbol == 'TUSD'):
        returned_price = math.ceil(returned_price * 100000000 ) / 100000000
        returned_price = format(returned_price, '.8f')
    elif ( symbol == 'HC' or symbol == 'MOD' or symbol == 'STRAT' or symbol == 'PPT' or symbol == 'INS' or symbol == 'KMD' or symbol == 'MTL' or symbol == 'ARK' or symbol == 'LUN' or symbol == 'NEBL' or symbol == 'SALT' or symbol == 'CLOAK' or symbol == 'WAN' or symbol == 'GXS' or symbol == 'GVT' or symbol == 'EDO' or symbol == 'RLC' or symbol == 'LSK' or symbol == 'NAS' or symbol == 'AION' or symbol == 'EOS' or symbol == 'PIVX' or symbol == 'NEBL' or symbol == 'AE' or symbol == 'VIA' or symbol == 'WTC' or symbol == 'WAVES' or symbol == 'NXS' or symbol == 'NANO' or symbol == 'NAV' or symbol == 'STEEM' or symbol == 'ICX' or  symbol == 'BNB' or symbol == 'ICX' or symbol == 'ONT' ):
        returned_price = math.ceil(returned_price * 10000000 ) / 10000000
        returned_price = format(returned_price, '.7f')
    elif ( symbol == 'DGD' or symbol == 'ZEC' or symbol == 'BCD' or symbol == 'XMR' or symbol == 'DASH' or  symbol == 'OMG' or symbol == 'BTG' or  symbol == 'XZC' or symbol == 'ZEN' or symbol == 'DCR' or symbol == 'MCO' or symbol == 'SKY' or symbol == 'REP' or symbol == 'ETC' or symbol == 'NEO'  or symbol == 'QTUM' or symbol == 'BCHABC' or symbol == 'BCHSV' or symbol == 'ETH' or symbol == 'LTC' ):
        returned_price = math.ceil(returned_price * 1000000 ) / 1000000
        returned_price = format(returned_price, '.6f')
        
    return returned_price

def trading_rule_amount_BTC( symbol, returned_amount ):

    returned_amount = float(returned_amount)

    if ( symbol == 'BTT' or  symbol == 'RCN' or  symbol == 'GO' or  symbol == 'POLY' or  symbol == 'MITH' or  symbol == 'REN' or  symbol == 'RVN' or  symbol == 'SYS' or symbol == 'QKC' or symbol == 'ZRX' or symbol == 'SUB' or symbol == 'DATA' or symbol == 'AGI' or symbol == 'SNM' or symbol == 'OAX' or symbol == 'FUN' or symbol == 'BQX' or symbol == 'GRS' or symbol == 'CMT' or symbol == 'REQ' or symbol == 'RNC' or  symbol == 'EVX' or symbol == 'WPR' or symbol == 'BAT' or symbol == 'MANA' or symbol == 'APPC' or symbol == 'GNT' or symbol == 'THETA' or symbol == 'LRC' or symbol == 'LEND' or symbol == 'DOCK' or symbol == 'KEY' or symbol == 'ZIL' or symbol == 'ADX' or symbol == 'PHX' or symbol == 'TNB' or symbol == 'BLZ' or symbol == 'CND' or symbol == 'ENG' or symbol == 'STORM' or symbol == 'SNGLS' or symbol == 'CVC' or symbol == 'ARDR' or symbol == 'SC' or symbol == 'ENJ' or symbol == 'TNT' or symbol == 'AST' or symbol == 'RDN' or symbol == 'NCASH' or symbol == 'LOOM' or symbol == 'NPXS' or symbol == 'QLC' or symbol == 'STORJ' or symbol == 'WABI' or symbol == 'VIB' or symbol == 'SNT' or symbol == 'BTS' or symbol == 'ARN' or symbol == 'CDT' or symbol == 'POWR' or symbol == 'IOST' or symbol == 'MFT' or symbol == 'BRD' or symbol == 'QSP' or symbol == 'YOYO' or symbol == 'DLT' or symbol == 'MTH' or symbol == 'XVG' or symbol == 'TRX' or symbol == 'VIBE' or symbol == 'XEM' or symbol == 'DENT' or symbol == 'WINGS' or symbol == 'GTO' or symbol == 'HOT' or symbol == 'IOTX' or symbol == 'DNT' or symbol == 'ELF' or symbol == 'LINK' or symbol == 'MDA' or symbol == 'BNT' or symbol == 'KNC' or symbol == 'POE' or symbol == 'FUEL' or symbol == 'BCPT' or symbol == 'OST' or symbol == 'AMB' or symbol == 'POA' or symbol == 'ADA' or  symbol == 'TRX' or  symbol == 'VET' or  symbol == 'XLM' or symbol == 'XRP' or  symbol == 'IOTA' or  symbol == 'NULS' or symbol == 'TUSD'):
        returned_amount =  math.floor( returned_amount )
    elif ( symbol == 'WTC' or  symbol == 'RLC' or  symbol == 'HC' or  symbol == 'MOD' or  symbol == 'AE' or  symbol == 'NAS' or symbol == 'LSK' or  symbol == 'NAV' or  symbol == 'MCO' or  symbol == 'STRAT' or  symbol == 'WAVES' or symbol == 'PIVX' or  symbol == 'PPT' or symbol == 'INS' or  symbol == 'KMD' or  symbol == 'MTL' or  symbol == 'ARK' or  symbol == 'NXS' or  symbol == 'VIA' or  symbol == 'STEEM' or  symbol == 'LUN' or  symbol == 'NEBL' or  symbol == 'SALT' or  symbol == 'OMG' or  symbol == 'CLOAK' or  symbol == 'AION' or  symbol == 'BTG' or  symbol == 'WAN' or  symbol == 'GXS' or  symbol == 'GVT' or  symbol == 'XZC' or  symbol == 'EDO' or symbol == 'NANO' or  symbol == 'BNB' or symbol == 'EOS' or symbol == 'ICX' or symbol == 'ETC' or symbol == 'NEO' or symbol == 'ONT' or symbol == 'QTUM' or symbol == 'LTC'):
        returned_amount = ( math.floor(returned_amount * 100) ) / 100
        returned_amount = format(returned_amount, '.2f')
    elif ( symbol == 'DCR' or symbol == 'ZEC' or  symbol == 'DGD' or  symbol == 'SKY' or symbol == 'ZEN' or  symbol == 'BCD' or  symbol == 'XMR' or  symbol == 'DASH' or  symbol == 'REP' or symbol == 'BCHABC' or symbol == 'BCHSV' or symbol == 'ETH' ):
        returned_amount = ( math.floor(returned_amount * 1000) ) / 1000
        returned_amount = format(returned_amount, '.3f')

    return returned_amount

def theory_1(symbol):

    # buy X using USDT with rate=(X/USDT)(askPrice) 
    # sell X to get BTC with rate=(X/BTC)(bidPrice)
    # sell BTC to get USDT with rate=(BTC/USDT)(bidPrice)
    # amount_x_from_usd = initial_cost /  float(get_depthData(symbol[0], 'USDT', 'askPrice'))  

    amount_x_from_usd = initial_cost /  X_USDT_ask  
    print("buy {} amount of {} using {} USD".format(amount_x_from_usd, symbol[0], initial_cost))
    amount_x_from_usd = amount_x_from_usd * 0.999
    amount_btc_from_x = amount_x_from_usd *  X_BTC_bid
    print("sell {} amount of {} to get {} BTC".format(amount_x_from_usd, symbol[0], amount_btc_from_x))
    amount_btc_from_x = amount_btc_from_x * 0.999
    btc_to_usd = amount_btc_from_x * BTC_USDT_bid
    btc_to_usd = btc_to_usd * 0.999
    return btc_to_usd

def theory_2(symbol):

    # buy BTC using USDT with rate=(BTC/USDT)(askPrice) 
    # buy X using BTC with rate=(X/BTC)(askPrice)
    # sell X to get USDT with rate=(X/USDT)(bidPrice)
   
    amount_btc_from_usd = initial_cost /  BTC_USDT_ask
    print("buy {} amount of BTC using {} USD".format(amount_btc_from_usd, initial_cost))
    amount_btc_from_usd = amount_btc_from_usd * 0.999
    amount_x_from_btc = amount_btc_from_usd *  1 / X_BTC_ask     
    print("buy {} amount of {} using {} amount of BTC".format(amount_x_from_btc, symbol[0], amount_btc_from_usd))
    amount_x_from_btc = amount_x_from_btc * 0.999
    x_to_usd = amount_x_from_btc * X_USDT_bid     
    x_to_usd = x_to_usd * 0.999

    return x_to_usd

def get_latest_rate(numerator, denominator):

    url = "https://api.binance.com/api/v3/ticker/price?symbol="

    symbol = numerator + denominator
    # ticker = client.get_orderbook_ticker( symbol = symbol )
    ticker = url + symbol
    r = requests.get(ticker)
    result = r.json()

    return float(result.get('price'))

def set_initial_cost(is_first_condition, X, numerator, denominator):

    initial_cost = 0

    first = bidPrice_and_askPrice(X, denominator)
    second = bidPrice_and_askPrice(X, numerator)
    third = bidPrice_and_askPrice(numerator, denominator)

    askPrice_first = float(first[1])
    askQty_first = float(first[3])
    
    bidPrice_second = float(second[0])
    bidQty_second = float(second[2])

    bidPrice_third = float(third[0])
    bidQty_third = float(third[2])

    first_total = askPrice_first * askQty_first
    # make it the same unit base
    second_total = bidPrice_second * bidQty_second * get_latest_rate(numerator, denominator)
    third_total = bidPrice_third * bidQty_third


    print("Current transaction pair : {}-{}-{}".format(denominator, numerator, X))
    print("{} / {} (売り成行) = {} {}".format(X, denominator, first_total, denominator))
    print("{} / {} (買い成行) = {} {}".format(X, numerator, second_total, denominator))
    print("{} / {} (買い成行) = {} {}".format(numerator, denominator, third_total, denominator))

    if( denominator == 'BNB' ):

        if first_total < 1.1 or second_total < 1.1 or third_total < 1.1:
            initial_cost = 1.1
        elif first_total > 4 and second_total > 4 and third_total > 4 :
            initial_cost = 4
        else:
            initial_cost = first_total
            if initial_cost > second_total :
                initial_cost = second_total
            if initial_cost > third_total :
                initial_cost = third_total

    elif( denominator == 'BTC' ):

        if first_total < 0.0028 or second_total < 0.0028 or third_total < 0.0028:
            initial_cost = 0.0028
        elif first_total > 0.004 and second_total > 0.004 and third_total > 0.004 :
            initial_cost = 0.004
        else:
            initial_cost = first_total
            if initial_cost > second_total :
                initial_cost = second_total
            if initial_cost > third_total :
                initial_cost = third_total

    elif( denominator == 'ETH' ):

        if first_total < 0.09 or second_total < 0.09 or third_total < 0.09:
            initial_cost = 0.09
        elif first_total > 0.35 and second_total > 0.35 and third_total > 0.35 :
            initial_cost = 0.35
        else:
            initial_cost = first_total
            if initial_cost > second_total :
                initial_cost = second_total
            if initial_cost > third_total :
                initial_cost = third_total

    elif( denominator == 'USDT' ):

        if first_total < 11 or second_total < 11 or third_total < 11:
            initial_cost = 11
        elif first_total > 25 and second_total > 25 and third_total > 25 :
            initial_cost = 25
        else:
            initial_cost = first_total
            if initial_cost > second_total :
                initial_cost = second_total
            if initial_cost > third_total :
                initial_cost = third_total

    print("initial_cost = {} {}".format(initial_cost, denominator))

    return initial_cost

    #      # X_BTC_total = float( get_depthData(numerator, 'BTC', 'bidPrice') ) * float( get_depthData(numerator, 'BTC', 'bidQty') ) * BTC_USDT_rate
    #     X_BTC_total = X_BTC_bid * float( get_depthData(numerator, 'BTC', 'bidQty') ) * BTC_USDT_rate
        
    #     # X_USDT_total =  float( get_depthData(numerator, 'USDT', 'askPrice') ) * float( get_depthData(numerator, 'USDT', 'askQty') )
    #     X_USDT_total =  X_USDT_ask * float( get_depthData(numerator, 'USDT', 'askQty') )
        
    #     if X_BTC_total > 100 and X_USDT_total > 100 :
    #         initial_cost = 100
    #     elif X_BTC_total < X_USDT_total:
    #         initial_cost = X_BTC_total
    #     else:
    #         initial_cost = X_USDT_total

    # # BTC_USDT_rate = float( client.get_symbol_ticker(symbol = 'BTCUSDT').get("price") )

    # if is_first_condition:

    #     # X_BTC_total = float( get_depthData(numerator, 'BTC', 'bidPrice') ) * float( get_depthData(numerator, 'BTC', 'bidQty') ) * BTC_USDT_rate
    #     X_BTC_total = X_BTC_bid * float( get_depthData(numerator, 'BTC', 'bidQty') ) * BTC_USDT_rate
        
    #     # X_USDT_total =  float( get_depthData(numerator, 'USDT', 'askPrice') ) * float( get_depthData(numerator, 'USDT', 'askQty') )
    #     X_USDT_total =  X_USDT_ask * float( get_depthData(numerator, 'USDT', 'askQty') )
        
    #     if X_BTC_total > 100 and X_USDT_total > 100 :
    #         initial_cost = 100
    #     elif X_BTC_total < X_USDT_total:
    #         initial_cost = X_BTC_total
    #     else:
    #         initial_cost = X_USDT_total

    #     print("X_BTC_total : {}".format(X_BTC_total))
    #     print("X_USDT_total : {}".format(X_USDT_total))
    #     print("BTC_USDT_rate : {}".format(BTC_USDT_rate))

    # else:

    #     # X_BTC_total = float( get_depthData(numerator, 'BTC', 'askPrice') ) * float( get_depthData(numerator, 'BTC', 'askQty') ) * BTC_USDT_rate
    #     X_BTC_total = X_BTC_ask * float( get_depthData(numerator, 'BTC', 'askQty') ) * BTC_USDT_rate
        
    #     # X_USDT_total =  float( get_depthData(numerator, 'USDT', 'bidPrice') ) * float( get_depthData(numerator, 'USDT', 'bidQty') )
    #     X_USDT_total =  X_USDT_bid * float( get_depthData(numerator, 'USDT', 'bidQty') )

    #     if X_BTC_total > 100 and X_USDT_total > 100 :
    #         initial_cost = 100
    #     elif X_BTC_total < X_USDT_total:
    #         initial_cost = X_BTC_total
    #     else:
    #         initial_cost = X_USDT_total

    #     print("X_BTC_total : {}".format(X_BTC_total))
    #     print("X_USDT_total : {}".format(X_USDT_total))
    #     print("BTC_USDT_rate : {}".format(BTC_USDT_rate))

    # return initial_cost

# def generate_csv( numerator, denominator, currency_tuple ):

#     filename = "report_"+numerator+"_"+denominator+"_X_0201.csv"

#     with open(filename,'a') as f:

#         writer = csv.writer(f)

#         header = '時間, '

#         for i in currency_tuple:
#             s = i+"/"+denominator+"(買い気配),"+i+"/"+denominator+"(売り気配),"+i+"/"+numerator+"(買い気配),"+i+"/"+numerator+"(売り気配),"+numerator+"/"+denominator+"(買い気配),"+numerator+"/"+denominator+"(売り気配),"
#             header += s
#         writer.writerow([header]) 

#         while True:

#             # JP_time_local = datetime.datetime.now()
#             JP_time_AWS = datetime.datetime.now() + datetime.timedelta(hours=9)

#             formatted_time =  JP_time_AWS.strftime("%H:%M:%S")
#             print("{}_{}_X : {} ".format(numerator, denominator, formatted_time))

#             row = formatted_time+", "

#             for i in currency_tuple:

#                 row += fetch_value(i, denominator)

#                 row += fetch_value(i, numerator)

#                 row += fetch_value(numerator, denominator)
    
#             writer.writerow([row]) 

#             print("done")

#             time.sleep(60)


