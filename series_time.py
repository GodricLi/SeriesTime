# _*_ coding=utf-8 _*_

import pandas as pd
import numpy as np


"""时间序列：创建以时间对象为索引（行名称）的Series或DateFrame"""
date = pd.Series(np.arange(60), index=pd.date_range('2017-03-22', periods=60))
print(date)
# 按月切片
print(date['2017-3'])
# 按天切片
print(date['2017-4-4'])
# 按年切片
print(date['2017'])
# 按时间段切片
print(date['2017-4-5':'2017-5-6'])

# resample()取样，支持各种运算
print(date.resample('W').sum())  # 按周取样后求和