import requests
from bs4 import BeautifulSoup

from plyer import notification

import time


def notifyRonak():
    title = "ALERT"
    message = f"Recent price drop on the item you've been looking for recently"
    notification.notify(title = title, message = message,app_icon = None, timeout = 10)

def price():
    URL = 'https://www.amazon.in/Lenovo-Executive-Backpack-Water-resistant-Uncompromised/dp/B08R7QTPKB/?_encoding=UTF8&pd_rd_w=ldB9g&pf_rd_p=ee853eb9-cee5-4961-910b-2f169311a086&pf_rd_r=HJSPPZ1M08KM5MFHDCJJ&pd_rd_r=0d31fe15-00d0-445c-9df8-d05f05504a73&pd_rd_wg=coDav&ref_=pd_gw_ci_mcx_mr_hp_atf_m'
    header = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}
    r = requests.get(URL, headers=header)
    s = BeautifulSoup(r.content, 'html.parser')
    # print(s.prettify())
    title = s.find(id="productTitle").get_text()
    print(title.strip())
    price = s.find(class_="a-offscreen").get_text()
    converted_price = price[1:]
    converted_price = float(converted_price)
    print(converted_price)
    if(converted_price > 700):
        notifyRonak()


while(True):
    price()
    time.sleep(60*60)