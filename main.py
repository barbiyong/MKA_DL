import json
from read_data import get_data
from save_ohlc import check_data_is_up_to_date

check_data_is_up_to_date()


def get_stock_active_name_list():
    with open('active_stock.json') as data_file:
        stock_names = json.load(data_file)
    return stock_names


def get_stock_name_of_template(first_date, last_date, tf, profit, highest_loss):
    tf = 'day'
    stocks = get_stock_active_name_list()
    for symbol in stocks:
        data = get_data(symbol, tf, first_date, last_date)

