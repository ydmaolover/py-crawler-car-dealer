# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:51:49 2019

@author: yudi.mao
"""

import re
import requests

province = requests.get('http://www.changan-mazda.com.cn/dictionary/city')
provinceid = re.findall('"id":"(.*?)",',province.text)[0:34]

city_list = list()
for i in range(0,34):
    cityurl = 'http://www.changan-mazda.com.cn/dictionary/city/' + provinceid[i]
    city = requests.get(cityurl)
    cityid = re.findall('"id":"(.*?)",', city.text)
    city_list.extend(cityid)

dea_name = list()
for j in range(0,len(city_list)):
    dealerurl = 'http://www.changan-mazda.com.cn/dictionary/dealer/' + city_list[j]
    dealer = requests.get(dealerurl)
    dlname = re.findall('"dea_name":"(.*?)",', dealer.text)
    dea_name.extend(dlname)

a = list()
for k in range(0, len(dea_name)):
    a.append(
             dea_name[k].encode('utf-8').decode('unicode_escape')
             )
