import json
import screener
import plot

# screener.get_stock_name_of_template('11/02/2016', '12/02/2016', 'day', 20, 5)

var = 1
while var == 1:  # This constructs an infinite loop
    input_val = input("scan(s) or plot(p): ")
    if input_val == 's':
        first_date, last_date = map(str, input("date a(ex.'11/02/2016'), date b('12/02/2016')  :").split(','))
        profit, highest_loss = map(float, input("profit, highest loss  :").split(','))
        print(first_date, last_date, profit, highest_loss)
        ret = screener.get_stock_name_of_template(first_date, last_date, 'day', profit, highest_loss)
        with open("screen_result.json", "w") as outfile:
            json.dump(ret, outfile)
    elif input_val == 'p':
        data = json.loads(open("screen_result.json").read())
        for n, item in enumerate(data['symbol']):
            print(data['symbol'][n], data['profit_return'][n], data['most_loss'][n])
        while var == 1:
            input_val = input("enter name: ")
            if input_val == 'exit':
                break
            try:
                if data['symbol'].index((input_val.upper())) is not None:
                    # print(data['symbol'].index(input_val))
                    index = data['symbol'].index(input_val)
                    plot.plot(data['symbol'][index], data['first_date'][index], data['last_date'][index])
            except ValueError:
                print("stock doesn't exits")
    else:
        break

# # open an HTML file on my own (Windows) computer
# url = "plot.html"
# webbrowser.open(url, new=2)

