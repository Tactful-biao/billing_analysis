#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import json
import matplotlib.pyplot as plt

food = spend_money = traffic = fruit = movies = bill = snacks = clothes = daily_necessities = 0
path = 'D:/a小程序/博客图片/python对账单进行分析/交流账单.txt'
records = [json.loads(line) for line in open(path)]
for i in range(705):
    items = records[i]
    if items['账目分类'] == '餐饮':
        food += float(items['账目金额'])
    elif items['账目分类'] == '花钱':
        spend_money += float(items['账目金额'])
    elif items['账目分类'] == '交通':
        traffic += float(items['账目金额'])
    elif items['账目分类'] == '水果':
        fruit += float(items['账目金额'])
    elif items['账目分类'] == '电影':
        movies += float(items['账目金额'])
    elif items['账目分类'] == '话费':
        bill += float(items['账目金额'])
    elif items['账目分类'] == '零食':
        snacks += float(items['账目金额'])
    elif items['账目分类'] == '服饰':
        clothes += float(items['账目金额'])
    elif items['账目分类'] == '日用品':
        daily_necessities += float(items['账目金额'])

plt.rcParams['font.sans-serif']=['SimHei']      
labels = ['餐饮','其他','交通','电影','话费','零食','水果','服饰','日用品']
sizes = [abs(int(food)),abs(int(spend_money)),abs(int(traffic)),abs(int(movies)),abs(int(bill)),abs(int(snacks)),abs(int(fruit)),abs(int(clothes)),abs(int(daily_necessities))]
colors = ['blue','green','yellowgreen','gold','lightskyblue','lightcoral','lightgray','lime','skyblue']
explode=(0.05,0,0,0,0,0,0,0,0)
plt.title(u'交流消费账单统计图\n\n')
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.legend(loc='upper right')
plt.show()
