from bs4 import BeautifulSoup
import requests
import csv

page = requests.get("http://www.bseindia.com/markets/equity/EQReports/mktwatchR.aspx?expandable=2&filter=gainer*all$all$")
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

rows = zip(company,LTP,Chg,PerChg)

with open('newfilePath1.csv', "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)