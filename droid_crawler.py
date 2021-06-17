# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import os
import requests
import time

captcha_string = 'Google의 시스템이 컴퓨터 네트워크에서 비정상적인 트래픽을 감지했습니다'.lower()


mal_keyword = ["malware", "virus", "악성코드", "바이러스", "scan",  "troj", "adware", "riskware", "backdoor", "dropper", "fake", "danger"]

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

# md5 sha256 pkg\n
#keyword = ["19162b063503105fdc1899f8f653b42d1ff4fcfcdf261f04467fad5f563c0270", 'malbus', 'fuck', 'shit']

start = time.time()

real_count = 0

f = open("./res_droids/finished_decom.txt", "r")

#618 * 3 requests needed

res = f.read().split('\n')[:-1]


f1 = open("./res_droids/detecting_result.txt", "a")
#f2 = open("", "w")

ctr = 0 

def rec_crawl(ctr):
  driver = webdriver.Chrome('chromedriver', options=options)
  driver.implicitly_wait(4)

  for data in res[ctr:]:
    print("Num {} strted \n".format(ctr))
    req_list = data.split(' ')
    for i in range(len(req_list)):
      success = False
      driver.get("https://google.com/search?q=" + req_list[i])
      time.sleep(0.5)
      html = driver.page_source
      html = html.lower()

      if captcha_string in html:
        print('We met captcha.. rebooting\n')
        driver.quit()
        time.sleep(10)
        rec_crawl(ctr) 
      
      for keyword in mal_keyword:
        if keyword in html:
          success = True
          print("Num {} : {} is Detected as a malware \n".format(ctr, req_list[1]))
          f1.write(("Num {} : {} is Detected as a malware \n".format(ctr, req_list[1])))
          break

      if success == True:
        break

    if success == False:
      print("Num {} : {} is Not Detected as a malware \n".format(ctr, req_list[1]))
      f1.write("Num {} : {} is Not Detected as a malware \n".format(ctr, req_list[1]))
    ctr += 1

rec_crawl(ctr)

print("time for 1000 req : {}sec".format(time.time() - start))