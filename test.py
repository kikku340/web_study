#-*- coding:utf-8 -*-
import urllib.request
import sys
import json
import time
from datetime import datetime

value_url = "https://c-cex.com/t/prices.json"
btc_url = "https://bitflyer.jp/api/echo/price"

headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

def get_price_zeny():
    request = urllib.request.Request(url=value_url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    ret = json.loads(html)
    str1 = ret['zny-btc']['lastbuy']
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print("1bitzeny = {0}satoshi\n".format(int(float(str1) * 100000000)))

def get_price_btc():
    request = urllib.request.Request(url=btc_url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    ret = json.loads(html)
    str1 = ret['mid']['']
    print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
    print("1btc = {0}yen\n".format(int(float(str1))))

while True:
    #get_price_zeny()
    get_price_btc()
    time.sleep(60)
