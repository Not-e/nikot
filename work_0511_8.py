# author: dqw_1519100068_0523（邓清文）
# 5月车牌预价

import datetime
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


def get_data(file_name):
    data = pd.read_csv(file_name)
    time = []
    personal_x_price = []
    personal_y_price = []
    for t, x1, y1 in zip(data['sort'], data['pers_lowest_price'], data['pers_average_price']):
        time.append([float(t)])
        personal_x_price.append([float(x1)])
        personal_y_price.append(float(y1))
    return time, personal_x_price, personal_y_price


def sec_data(x, y):
    x_n = []
    y_n = []
    for i in range(1, len(x1)):
        if i > 7 and i < 13:
            x_n.append(x[i])
            y_n.append(y[i])
        elif i > 30 and i < 36:
            x_n.append(x[i])
            y_n.append(y[i])
        else:
            continue
    return x_n, y_n


def draw_pc(t, x1, y1):
    plt.figure(figsize=(8, 6))
    t_n, x1_n = sec_data(t, x1)
    lr1 = linear_model.LinearRegression()
    lr1.fit(t_n, x1_n)
    print(lr1.predict(len(x1) + 1))
    plt.scatter(t_n, x1_n, color='blue')
    plt.plot(t, lr1.predict(t), 'b--', linewidth=1.3, label='pers_lowest_hprice')
    t_n, y1_n = sec_data(t, y1)
    lr2 = linear_model.LinearRegression()
    lr2.fit(t_n, y1_n)
    print(lr2.predict(len(x1) + 1))
    plt.scatter(t_n, y1_n, color='r')
    plt.plot(t, lr2.predict(t), 'r--', linewidth=1.3, label='pers_average_hprice')
    plt.plot(t, x1, 'b', linewidth=1.3, label='pers_lowest_price')
    plt.plot(t, y1, 'r', linewidth=1.3, label='pers_average_price')
    plt.legend()
    # plt.savefig('work8_h_5_5.jpeg')
    plt.show()


t, x1, y1 = get_data('work8.csv')
draw_pc(t, x1, y1)

# 5_5   36037.31843575  37680.18435754
# 5_4   40207.80858676  42207.72119857
# 4_5   33938.30409357  35282.4128655
# 4_4   38100.74906367  39801.94990637
# 2018.4    32100   	34455
# 历史最高     35000	    37805
