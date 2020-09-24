from bs4 import BeautifulSoup
import csv

import requests
import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hack.settings')

import django
django.setup()

from untact.models import Info

cookies = {
    'ASP.NET_SessionId': 'hqyrs5qr5fixs4o00qqtbiyd',
    'RecentSWs': 'wgMktQ6AaG0lOPz1vvor2Q==',
    'PCID': '16009459628772562619581',
    '__utma': '186092716.2028395295.1600945963.1600945963.1600945963.1',
    '__utmc': '186092716',
    '__utmz': '186092716.1600945963.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmt': '1',
    '_fbp': 'fb.1.1600945963468.2011241569',
    '_ga': 'GA1.2.2028395295.1600945963',
    '_gid': 'GA1.2.30163615.1600945963',
    '_gat_UA-166644337-1': '1',
    '__utmb': '186092716.3.10.1600945963',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'text/html, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://ticket.yes24.com',
    'Referer': 'http://ticket.yes24.com/Search/%ec%98%a8%eb%9d%bc%ec%9d%b8',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
}

SearchType={'15456':'공연/콘서트','15457':'연극/뮤지컬','15458':'연극/뮤지컬','15459':'공연/콘서트','15460':'전시/관람'}

data = {
  'SearchText': '\uC628\uB77C\uC778',
  'SearchSubText': '',
  'SearchType': '',
  'BookingType': '',
  'PerfCurPage': '',
  'PageSize': '10',
  'SortType': '1'
}

def get_data():
  contents = []
  for search in SearchType.keys():
    num=1
    data['PerfCurPage']=num
    data['SearchType']=search
    response = requests.post('http://ticket.yes24.com/New/Search/Ajax/axPerfList.aspx', headers=headers, cookies=cookies, data=data, verify=False)
    while response.text.split()!=[]:
      response = requests.post('http://ticket.yes24.com/New/Search/Ajax/axPerfList.aspx', headers=headers, cookies=cookies, data=data, verify=False)

      soup = BeautifulSoup(response.text, 'html.parser')

      select = soup.select(
        '.srch-list-item'
      )
      
      for content in select:
        contentdict={}
      
        contentdict['category']=SearchType[search]
        date = content.select('div')[2].get_text().split('~')

        enddate = datetime.datetime.strptime(date[1], format('%Y.%m.%d'))
        if enddate < datetime.datetime.now():
          break
        
        contentdict['startdate'] = datetime.datetime.strptime(date[0], format('%Y.%m.%d'))
        contentdict['enddate'] = datetime.datetime.strptime(date[1], format('%Y.%m.%d'))

        if content.select_one('div>a>img'):
          contentdict['href'] = 'http://ticket.yes24.com/'+content.find('a')['href']
          contentdict['img'] = content.select_one('a').find('img')['src']

        if content.select_one('div>.item-tit'):
          contentdict['title']=content.select_one('.item-tit>a').get_text()
        
        contentdict['actor'] = get_actor(contentdict['href'])
        
        contents.append(contentdict)   
      num+=1
      data['PerfCurPage']=num

  return contents

def get_actor(href):
  response = requests.post(href)
  soup = BeautifulSoup(response.text, 'html.parser')
  select = soup.select('td')[3].get_text()

  return select

def save_csv():
  contents=get_data()

  for content in contents:
    print(content)

  with open('result.csv','w', encoding='UTF-8-sig', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ['category','startdate','enddate','href','img','title','actor'])
    writer.writeheader()
    for content in contents:
      writer.writerow(content)


if __name__=='__main__':
  contents=get_data()
  for content in contents:
    Info(category= content['category'],
    startdate=content['startdate'], enddate=content['enddate'], 
    href = content['href'], img=content['img'],
    title=content['title'], actor=content['actor']).save()
