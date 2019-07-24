# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:39:38 2019

@author: yudi.mao
"""

import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#lexus
result=[]
driver=webdriver.Firefox(log_path=r"E:\geckodriver.log")
wait=WebDriverWait(driver,10)
driver.get('http://www.lexus.com.cn/dealer')
province=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#select-prov.form-control')))
province.click()
province_nm=province.find_elements_by_css_selector('option')
for prov in province_nm[1:]:
    print('正在爬取%s...'%prov.text)
    prov.click()
    city=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#select-city.form-control')))
    city.click()
    #设置休眠间隔
    time.sleep(1)
    city_nm=city.find_elements_by_css_selector('option')
    for city in city_nm[1:]:
        #print('正在爬取的是{}'.format(city.text))
        city.click()
        time.sleep(1)
        #Relocate
        map_list = driver.find_element_by_id('map-list')
        dealer_list = map_list.find_elements_by_css_selector('li')
        dealer_last=[i.text for i in dealer_list]
        print('{}的商户列表是：{}'.format(city.text,dealer_last))
        result.extend(dealer_last)
driver.quit()
mchnt_name=pd.DataFrame(result,columns=['mchnt_name'])