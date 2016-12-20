import json
import time

import save_ohlc

def get_data(stock_name):

    dohlcv_120 = json.loads(open("files/" + stock_name + "_120.json").read())
    dohlcv_day = json.loads(open("files/" + stock_name + "_day.json").read())
    dohlcv_week = json.loads(open("files/" + stock_name + "_week.json").read())
    dohlcv_month = json.loads(open("files/" + stock_name + "_month.json").read())
    return dohlcv_120, dohlcv_day, dohlcv_week, dohlcv_month


def check_data_is_up_to_date():
    f = open('files/log', 'r')
    first_line = f.readline()
    f.close()

    if str(first_line) == str(time.strftime("%Y/%m/%d")):
        print('\n --- All data is up to date ---')
    else:
        print('File is not up to date \n update files...')
        save_ohlc.main()
        f = open('files/log', 'w')
        f.write(time.strftime("%Y/%m/%d"))
        f.close()
        print('\n --- All data is up to date ---')

check_data_is_up_to_date()
