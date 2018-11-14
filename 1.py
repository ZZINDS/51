# -*- coding: utf-8 -*-
"""
@Time    : 2018/11/14 15:30
@Author  : ZZINDS
@Site    : 
@File    : 1
@Software: PyCharm
"""
import pickle

f = open('data1.pkl', 'rb')
info = pickle.load(f)
print(info)