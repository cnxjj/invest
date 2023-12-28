import openpyxl as op
import pandas as pd
import xlwings as xw
from openpyxl import load_workbook
from datetime import datetime

# 判断给定日期是周几，返回0-6
def isweek(date):
    # date_f = datetime.strptime(date, "%Y%m%d") # 字符串转为日期格式
    week = datetime.weekday(date)
    return(week)

        
beg = '2023-09-13'  # 开始日期



print(isweek(beg))