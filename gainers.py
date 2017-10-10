from bs4 import BeautifulSoup
import requests
import csv
import numpy as np
import pandas as pd

def gainlose(url,f):
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find( "table", {"id":"ctl00_ContentPlaceHolder1_grd1"} )

    tr = table.find_all('a', class_='tablebluelink')
    company = []
    for i in range(len(tr)):
        company.append(tr[i].text)

    tr = table.find_all('td', class_='TTRow_right')

    LTP = []
    for i in range(len(tr)):
        LTP.append(tr[i].text)

    Chg = []
    for i in range(len(LTP)):
        if i+1 < len(LTP):
            Chg.append(LTP[i+1])
    PC = table.find_all('td', attrs={'style': 'background-color:#DFDEDD;height:15px;width:40px;'})

    PerChg = []
    for i in range(len(PC)):
        PerChg.append(PC[i].text)

    company.insert(0,'Company')
    LTP.insert(0,'LTP')
    Chg.insert(0,'Change')
    PerChg.insert(0,'%Change')
    [str(i) for i in LTP]
    [str(i) for i in Chg]
    [str(i) for i in company]
    
    rows = zip(company,LTP,Chg)

    with open(f + '.csv', "w") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
#             print(row, '\n')
    
    
lose = 'http://www.bseindia.com/markets/equity/EQReports/mktwatchR.aspx?expandable=2&filter=loser*all$all$'
gain = 'http://www.bseindia.com/markets/equity/EQReports/mktwatchR.aspx?expandable=2&filter=gainer*all$all$'
print('\t\t','Top Gainers Today')
data = pd.read_csv('gainer.csv')
print(data.head(10))
gainlose(gain, 'gainer')
print('\n\t', 'Top Losers Today', '\n')
gainlose(lose, 'loser')
data = pd.read_csv('loser.csv')
print(data.head(10))
