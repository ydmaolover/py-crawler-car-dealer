# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:03:03 2019

@author: yudi.mao
"""

import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#东风起亚
result=[]
driver=webdriver.Firefox(log_path=r"E:\geckodriver.log")
wait=WebDriverWait(driver,20)
driver.get('http://dealer.peugeot.com.cn/')
province=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#sp.sim-pr')))
province.click()
province_nm=province.find_elements_by_css_selector('option')
for prov in province_nm[1:]:
    print('正在爬取%s...'%prov.text)
    prov.click()
    time.sleep(1)
    city=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'select#sc.sim-ci')))
    city.click()
    time.sleep(1)
    city_nm=city.find_elements_by_css_selector('option')
    for city in city_nm[1:]:
        #print('正在爬取的是{}'.format(city.text))
        city.click()
        time.sleep(1)
        serv_list=driver.find_element_by_id('sd')
        dealer_list=serv_list.find_elements_by_css_selector('option')
        dealer_last=[i.text for i in dealer_list]
        #去除‘经销商’
        del dealer_last[0]
        print('{}的商户列表是：{}'.format(city.text,dealer_last))
        result.extend(dealer_last)
        time.sleep(1)
driver.quit()
mchnt_name=pd.DataFrame(result,columns=['mchnt_name'])