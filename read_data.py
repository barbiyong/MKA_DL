import json
import time


def get_data(stock_name, tf, first_date, last_date):

    dohlcv = json.loads(open("files/" + stock_name + "_" + tf + ".json").read())
    if last_date == 0:
        try:
            last_date_index = -2
        except TypeError:
            return None
        except ValueError:
            return None
    else:
        try:
            last_date_index = dohlcv['date'].index(last_date)
        except TypeError:
            return None
        except ValueError:
            return None
    # print(last_date_index)
    if first_date == 0:
        try:
            first_date_index = 0
        except TypeError:
            return None
        except ValueError:
            return None
    else:
        try:
            first_date_index = dohlcv['date'].index(first_date)
        except TypeError:
            return None
        except ValueError:
            return None
    # print(first_date_index)

    dohlcv['date'] = dohlcv['date'][first_date_index:last_date_index+1]
    dohlcv['open'] = dohlcv['open'][first_date_index:last_date_index+1]
    dohlcv['close'] = dohlcv['close'][first_date_index:last_date_index+1]
    dohlcv['high'] = dohlcv['high'][first_date_index:last_date_index+1]
    dohlcv['low'] = dohlcv['low'][first_date_index:last_date_index+1]
    dohlcv['volume'] = dohlcv['volume'][first_date_index:last_date_index+1]

    return dohlcv
