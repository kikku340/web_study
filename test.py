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

def get_price(url, coin_name, price_str):
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')

        ret = json.loads(html)
        if not coin_name:
            return ret[price_str]
        return ret[coin_name][price_str]


value_zny = get_price(value_url, 'zny-btc', 'lastbuy')
value_btc = get_price(btc_url, "", 'mid')
print("1zny = {0}yen\n".format(round(float(value_btc * value_zny), 3)))
