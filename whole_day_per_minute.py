import urllib
import re
import json



while (True):
    answer=raw_input("Enter a stock symbol, to get one minute data for this day, up to now ")
    
    html_text=urllib.urlopen('https://finance-yql.media.yahoo.com/v7/finance/chart/'+answer+'?period2=1438610906&period1=1438265306&interval=1m&indicators=quote&includeTimestamps=true&includePrePost=true&events=div%7Csplit%7Cearn&corsDomain=finance.yahoo.com')

    data = json.load(html_text)


    open_data=data['chart']['result'][0]['indicators']['quote'][0]['open']



    for i in range(len(open_data)-1):
        print open_data[i]


    query=raw_input("Do you want to search for more stocks? y/n ")
    if query in "yY":
        continue
    else:
        break
