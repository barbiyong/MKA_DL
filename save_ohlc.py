import numpy as np
import pandas
import json
import time
from collections import OrderedDict


def get_stock_data(stock_name, time_frame):
    tmp_list = {}
    data_list = OrderedDict()
    candle_length = 200
    url_d = 'http://devapi.marketanyware.com/Test/OHLC.aspx?DL=1&Stock=' + stock_name + '&period=day'
    url_w = 'http://devapi.marketanyware.com/Test/OHLC.aspx?DL=1&Stock=' + stock_name + '&period=week'
    url_m = 'http://devapi.marketanyware.com/Test/OHLC.aspx?DL=1&Stock=' + stock_name + '&period=month'
    url_1h = 'http://devapi.marketanyware.com/Test/OHLC.aspx?DL=1&Stock=' + stock_name + '&period=Hour'
    url_2h = 'http://devapi.marketanyware.com/Test/OHLC.aspx?DL=1&Stock=' + stock_name + '&period=2Hour'

    if time_frame is 'day':
        url = url_d
    elif time_frame is 'week':
        url = url_w
    elif time_frame is 'month':
        url = url_m
    elif time_frame is 'hour':
        url = url_1h
    elif time_frame is '2Hour':
        url = url_2h

    try:
        stock_data_input = pandas.io.parsers.read_csv(url, sep=',')
    except pandas.io.common.CParserError:
        return None

    tmp_list['date'] = np.array(stock_data_input['Date'])

    if len(tmp_list['date']) < candle_length:
        candle_length = len(tmp_list['date'])

    # get data from web
    data_list['date'] = np.array(stock_data_input['Date'])
    data_list['open'] = np.array(stock_data_input['Op'])
    data_list['high'] = np.array(stock_data_input['High'])
    data_list['low'] = np.array(stock_data_input['Low'])
    data_list['close'] = np.array(stock_data_input['Close'])
    data_list['volume'] = np.array(stock_data_input['Volume'])

    data_length = len(data_list['date'])

    # convert to list
    data_list['date'] = np.array(data_list['date'][data_length - candle_length:data_length]).tolist()
    data_list['open'] = np.array(data_list['open'][data_length - candle_length:data_length]).tolist()
    data_list['high'] = np.array(data_list['high'][data_length - candle_length:data_length]).tolist()
    data_list['low'] = np.array(data_list['low'][data_length - candle_length:data_length]).tolist()
    data_list['close'] = np.array(data_list['close'][data_length - candle_length:data_length]).tolist()
    data_list['volume'] = np.array(data_list['volume'][data_length - candle_length:data_length]).tolist()

    return data_list


def get_stock_active_name_list():
    with open('active_stock.json') as data_file:
        stock_names = json.load(data_file)
    return stock_names


def main():
    stock_names = get_stock_active_name_list()
    # stock_names = ['AOT']
    for s in stock_names:
        print('get data of stock : '+s)
        with open("files/"+s+"_120.json", "w") as outfile_2h:
            json.dump(get_stock_data(s, '2Hour'), outfile_2h)
        with open("files/" + s + "_day.json", "w") as outfile_day:
            json.dump(get_stock_data(s, 'day'), outfile_day)
        with open("files/" + s + "_week.json", "w") as outfile_week:
            json.dump(get_stock_data(s, 'week'), outfile_week)
        with open("files/"+s+"_month.json", "w") as outfile_month:
            json.dump(get_stock_data(s, 'month'), outfile_month)


def check_data_is_up_to_date():
    f = open('files/log', 'r')
    first_line = f.readline()
    f.close()

    if str(first_line) == str(time.strftime("%Y/%m/%d")):
        print('\n --- All data is up to date ---')
    else:
        print('File is not up to date \n update files...')
        main()
        f = open('files/log', 'w')
        f.write(time.strftime("%Y/%m/%d"))
        f.close()
        print('\n --- All data is up to date ---')