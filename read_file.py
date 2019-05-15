import csv
import os
import numpy as np
import pandas as pd

# 使用 I/O
def read_file(filename):
    temp_data = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        birth_head = next(csv_reader)
        print(birth_head)
        for row in csv_reader:
            print(row)
            temp_data.append(row)
    # print(temp_data)

# 使用 pandas
def read_file_by_pd(filename):
    temp_data = []
    df = pd.read_csv(filename, nrows=53000, encoding='gbk', error_bad_lines=False)
    print(df.shape)
    print(df.info())
    print(df.head())
    print(df.tail())

if __name__ == '__main__':
    # read_file('./read_files/out1.csv')
    read_file_by_pd('./read_files/out1.csv')