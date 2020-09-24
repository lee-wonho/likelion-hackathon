import requests
import json

headers = {
    'authority': 'api-ticketfront.interpark.com',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'origin': 'https://tickets.interpark.com',
    #'sec-fetch-site': 'same-site',
    #'sec-fetch-mode': 'cors',
    #'sec-fetch-dest': 'empty',
    'referer': 'https://tickets.interpark.com/search?keyword=%EC%98%A8%EB%9D%BC%EC%9D%B8',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    #'cookie': 'pcid=159903650934795319; OAX=3F8qEV9PW2MADwmg; _fbp=fb.1.1599036510305.479359702; _gcl_aw=GCL.1599036510.EAIaIQobChMI3bbkkIvK6wIVQ5_CCh2LhQCtEAYYASABEgLYUPD_BwE; _ga=GA1.2.870487135.1599036511; _trs_id=eY%3E471%3F742%3E5733%3E3; _gac_UA-93337025-1=1.1600612662.CjwKCAjw-5v7BRAmEiwAJ3DpuH1myhkKA0S9ZvkE3QvkHYFHPQie3Jx6YselnGZ9-rjrBAuxoEYCFBoCSNkQAvD_BwE; _gac_UA-93889457-1=1.1600612662.CjwKCAjw-5v7BRAmEiwAJ3DpuH1myhkKA0S9ZvkE3QvkHYFHPQie3Jx6YselnGZ9-rjrBAuxoEYCFBoCSNkQAvD_BwE; _ACU124043=1599036511894169194.1600612663346.3.0.169194S9RPUVXK7YBBY.0.0.0.....; _gid=GA1.2.1632287148.1600829105',
}

params = (
    ('filter', '(bookableyn:Y OR bookableyn:D)'),
    ('q', '\uC628\uB77C\uC778'),
    ('rows', '20'),
    ('start', '0'),
    ('userCookie', ''),
)

response = requests.get('https://api-ticketfront.interpark.com/v1/search/ticket/search', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://api-ticketfront.interpark.com/v1/search/ticket/search?filter=%28bookableyn%3AY%20OR%20bookableyn%3AD%29&q=%EC%98%A8%EB%9D%BC%EC%9D%B8&rows=20&start=0&userCookie=', headers=headers)
result_dict = json.loads(response.text)

#print(result_dict)
#with open('data_inter.json', 'w', encoding='UTF-8') as outfile:
    #json.dump(result_dict, outfile, ensure_ascii=False)

print(result_dict['common']['timestamp'])


for goods in result_dict['data']['docs']:
    start_date = goods['registerdateforweb']
    code = goods['goodscode']
    end_date = goods['enddate']
    title = goods['goodsname']
    image = goods['imagepath']
    players = goods['playernames']
    players = players.replace(' ', '').split(',')[0:-1] if players is not None else []
    category = goods['kindofgoodsname']
    href = f'http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode={code}'
    print(title)
    print(category)
    print(players,end='\n'*2)
