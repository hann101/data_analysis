import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
import glob, os, sys

df1 = pd.read_excel('suppliers.xlsx', sheet_name='suppliers_2013', index_col=None)
df1
data = [
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx'
]
name = [
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013'
]
df1['file_from'] = data
df1['sheetname'] = name

df1_2 = pd.read_excel('suppliers.xlsx', sheet_name='suppliers_2014', index_col=None)
df1_2
data = [
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx',
    'suppliers.xlsx'
]
name = [
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014'
]
df1_2['file_from'] = data
df1_2['sheetname'] = name

df2 = pd.read_csv('suppliers_2016.csv')
data = [
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv',
    'suppliers_2016.csv'
]
name = [
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016',
    'suppliers_2016'
]
df2['file_from'] = data
df2['sheetname'] = name

df3 = pd.read_excel('suppliers.xls', sheet_name='suppliers_2013')
data = [
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls'
]
name = [
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013',
    'suppliers_2013'
]
df3['file_from'] = data
df3['sheetname'] = name

df3_2 = pd.read_excel('suppliers.xls', sheet_name='suppliers_2014')
data = [
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls',
    'suppliers.xls'
]
name = [
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014',
    'suppliers_2014'
]
df3_2['file_from'] = data
df3_2['sheetname'] = name

df_n = pd.read_csv('item_numbers_to_find.csv', header=None)
numb = df_n.to_numpy()
df11 = df1[(df1['Item Number'] == numb[0][0]) | (df1['Item Number'] == numb[1][0]) | (df1['Item Number'] == numb[2][0]) |
          (df1['Item Number'] == numb[3][0]) | (df1['Item Number'] == numb[4][0])]

df11_2 = df1_2[(df1_2['Item Number'] == numb[0][0]) | (df1_2['Item Number'] == numb[1][0]) | (df1_2['Item Number'] == numb[2][0]) |
          (df1_2['Item Number'] == numb[3][0]) | (df1_2['Item Number'] == numb[4][0])]

df22 = df2[(df2['Item Number'] == numb[0][0]) | (df2['Item Number'] == numb[1][0]) | (df2['Item Number'] == numb[2][0]) |
          (df2['Item Number'] == numb[3][0]) | (df2['Item Number'] == numb[4][0])]

df33 = df3[(df3['Item Number'] == numb[0][0]) | (df3['Item Number'] == numb[1][0]) | (df3['Item Number'] == numb[2][0]) |
          (df3['Item Number'] == numb[3][0]) | (df3['Item Number'] == numb[4][0])]

df33_2 = df3_2[(df3_2['Item Number'] == numb[0][0]) | (df3_2['Item Number'] == numb[1][0]) | (df3_2['Item Number'] == numb[2][0]) |
          (df3_2['Item Number'] == numb[3][0]) | (df3_2['Item Number'] == numb[4][0])]

re1 = df11.append(df22)
re1 = re1.append(df11_2)
re1 = re1.append(df33_2)
result = re1.append(df33)
def change_row(data):
    result = ''
    if isinstance(data, int):
        return data
    else:
        if data[0] == '$':
            result = data.replace('$', '').replace(',', '')
            return result.split('.')[0]
        else:
            return data
result['Cost'] = result['Cost'].apply(change_row)

result.to_csv('outpuy_hyomin.csv', index=False, header=None)