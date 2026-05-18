# imports
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from time import sleep
import csv

# key info
livepage_address = "https://www.bbc.co.uk/news/live/c99l70zy1j7t"
my_headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:84.0) Gecko/20100101 Firefox/84.0"}

visits = 0

# set to run every minute for 12 hours
while visits < 720:
    req = requests.get(livepage_address, headers = my_headers)
    soup = bs(req.content)
    for x in soup.find('span', class_ = "ssrcss-798imn-CounterStringContainer e1naroyk0"):
        d = x.text
        time = str(dt.now())
        with open("bbc_live_data.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([d, time])
    visits = visits+1
    sleep(60)
