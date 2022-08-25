# weather_project1.py
import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=109')
soup = BeautifulSoup(response.content, 'html.parser')

result=soup.find_all('div', {'class':'over-scroll'})
print(result[1])
table = result[1].find('table', { 'class': 'table-col' })    # <table class="table-col">을 찾음
#print(table)
.0
data = []
for tr in table.find_all('tr'): 
    #print(tr.select('.midterm-city'))
    td_city=tr.select('.midterm-city')
    if len(td_city)>0:
        city=td_city[0].text
        #print(city)

        tds = list(tr.find_all('td'))
        if city=='서울':
            tds=tds[1:]
        #print(tds)
        
        temp1 = tds[1].text 
        temp2 = tds[2].text
        temp3 = tds[3].text
        data.append([city, temp1, temp2, temp3])

print(data)