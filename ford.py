# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:59:14 2019

@author: yudi.mao
"""

import re
import requests
import pandas as pd

city = requests.get('https://www.ford.com.cn/content/ford/cn/zh_cn/configuration/application-and-services-config/provinceCityDropDowns.multiFieldDropdown.data')
city_list = re.findall('"cityValue":"(.*?)"}',city.text)

df = pd.DataFrame(columns = ['city', 'dealer'])
city = list()
dealer = list()

for i in range(0,len(city_list)):
    r = requests.get('https://yuntuapi.amap.com/datasearch/local?s=rsv3&key=1891d0f847c0a210a88015fdd4c3bc46&extensions=all&language=en&enc=utf-8&output=jsonp&&sortrule=_distance:1&autoFitView=true&panel=result&keywords=&limit=100&sortrule=_id:1&tableid=55adb0c7e4b0a76fce4c8dd6&radius=50000&platform=JS&logversion=2.0&sdkversion=1.4.2&appname=http://www.ford.com.cn/dealer/locator?intcmp=hp-return-fd&csid=6F094767-5285-454B-BC73-0D18F9C7223B&center=104.066541,30.572269&city=' + city_list[i])
    dl = re.findall('"_name":"(.*?)",',r.text)
    if len(dl):
        dealer.extend(dl)
        ct = [city_list[i]] * len(dl)
        city.extend(ct)

df['city'] = city
df['dealer'] = dealer
df1 = df.drop_duplicates(['dealer'])     



