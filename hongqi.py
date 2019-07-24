# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:26:27 2019

@author: yudi.mao
"""

import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#一汽红旗
result=[]
driver=webdriver.Firefox(log_path=r"E:\geckodriver.log")
wait=WebDriverWait(driver,10)
driver.get('http://www.faw-hongqi.com.cn/server/wd/2')
province=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#map_province_id.sel_sel')))
province.click()
province_nm=province.find_elements_by_css_selector('option')
for prov in province_nm[1:]:
    print('正在爬取%s...'%prov.text)
    prov.click()
    city=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#map_city_id.sel_sel2')))
    city.click()
    #设置休眠间隔
    time.sleep(1)
    city_nm=city.find_elements_by_css_selector('option')
    for city in city_nm[1:]:
        #print('正在爬取的是{}'.format(city.text))
        city.click()
        time.sleep(1)
        dealer_list=driver.find_elements_by_css_selector('div.h3')
        dealer_last=[i.text for i in dealer_list]
        print('{}的商户列表是：{}'.format(city.text,dealer_last))
        result.extend(dealer_last)
driver.quit()
mchnt_name=pd.DataFrame(result,columns=['mchnt_name'])