import json
import utils
from read_data import get_data
from save_ohlc import check_data_is_up_to_date


# check_data_is_up_to_date()


def get_stock_active_name_list():
    with open('active_stock.json') as data_file:
        stock_names = json.load(data_file)
    return stock_names


def get_stock_name_of_template(first_date, last_date, tf, profit, highest_loss):
    stocks = get_stock_active_name_list()
    profit_return = None
    most_loss = None
    # stocks = ['AOT']
    ret_dict = dict()
    ret_dict['symbol'] = []
    ret_dict['profit_return'] = []
    ret_dict['most_loss'] = []
    ret_dict['first_date'] = []
    ret_dict['last_date'] = []
    for symbol in stocks:
        data = get_data(symbol, tf, first_date, last_date)
        try:
            profit_return = utils.calculate_profit(data['close'])
            most_loss = utils.most_loss(data['close'])
        except TypeError:
            pass
        # print(profit_return, most_loss)
        if profit_return is not None and most_loss is not None:
            if profit_return > profit and most_loss < highest_loss:
                print(symbol, profit_return, most_loss)
                ret_dict['symbol'].append(symbol)
                ret_dict['profit_return'].append(profit_return)
                ret_dict['most_loss'].append(most_loss)
                ret_dict['first_date'].append(first_date)
                ret_dict['last_date'].append(last_date)
    return ret_dict
