#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 10:21:51 2017

@author: ajay
"""

from bs4 import BeautifulSoup
import requests


#losers url
url = 'http://www.bseindia.com/markets/equity/EQReports/mktwatchR.aspx?expandable=2&filter=loser*all$all$'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find( "table", {"id":"ctl00_ContentPlaceHolder1_grd1"} )

tr = table.find_all('a', class_='tablebluelink')

#getting all company names
company = []
for i in range(len(tr)):
    company.append(tr[i].text)

tr = table.find_all('td', class_='TTRow_right')

# LTP of a company
LTP = []
for i in range(len(tr)):
    LTP.append(tr[i].text)

#change of a company in Chg list
Chg = []
for i in range(len(LTP)):
    if i+1 < len(LTP):
        Chg.append(LTP[i+1])
    
#changing datatype of all elements of lists to string
[str(i) for i in LTP]
[str(i) for i in Chg]
[str(i) for i in company]

#slicing for top 5 only
LTP = LTP[0:5]
Chg = Chg[0:5]
company = company[0:5]