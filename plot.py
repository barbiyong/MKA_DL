from math import pi
import read_data as rd
import pandas as pd

from bokeh.plotting import figure, show, output_file


def plot(stock_name, first_date, last_date):
    tf = 'day'
    df = pd.DataFrame(rd.get_data(stock_name, tf, first_date, last_date))
    df["date"] = pd.to_datetime(df["date"])

    mids = (df.open + df.close) / 2
    spans = abs(df.close - df.open)

    inc = df.close > df.open
    dec = df.open > df.close
    nor = df.close = df.open
    w = 12 * 60 * 60 * 1000  # half day in ms

    output_file("candlestick.html", title="candlestick.py example")

    TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

    p = figure(x_axis_type="datetime", tools=TOOLS, plot_height=480, plot_width=720, toolbar_location="right")

    p.segment(df.date, df.high, df.date, df.low, color="black")
    p.rect(df.date[inc], mids[inc], w, spans[inc], fill_color="#2ECC71", line_color="black")
    p.rect(df.date[dec], mids[dec], w, spans[dec], fill_color="#F2583E", line_color="black")
    p.rect(df.date[nor], mids[nor], w, spans[nor], fill_color="black", line_color="black")

    p.title = "Candlestick of" + str(stock_name)
    p.xaxis.major_label_orientation = pi / 4
    p.grid.grid_line_alpha = 0.3

    show(p)  # open a browser
