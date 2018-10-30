# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
import csv
import time
url = "http://hz.58.com/pinpaigongyu/pn/{page}/?minprice=500_4000"

# 已完成的页数序号，初时为0
page = 0

csv_file = open("renthz.csv", "w")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    time.sleep(1)
    print("fetch: ", url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text, 'html.parser')
    house_list = html.select(".list > li")

    # 循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = "http://hz.58.com/%s" % (house.select("a")[0]["href"])
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select(".money")[0].select("b")[0].string
        csv_writer.writerow(
            [house_title, house_location, house_money, house_url])

csv_file.close()
