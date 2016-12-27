def calculate_profit(data):
    return round(((data[-1] - data[0]) / data[0]) * 100, 2)


def most_loss(data):
    min_val = min(data)
    # print(data[0], type(data[0]), min_val, type(min_val))
    ret = round(((data[0] - min_val) / min_val) * 100, 2)
    if ret == 0:
        print(data[0], min_val[0])
    return ret
