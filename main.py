import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
url = 'https://xhamster19.desi'

videoUrls = []
for page in range(1,2):
	print('Page ',page)
	soup = BeautifulSoup(requests.get(url+'/best/year-2022/' +str(page),'lxml').text)
	videoUrls.extend([i.get('href') for i in soup.find_all('a','thumb-image-container')])
tagsList = []	
for video in videoUrls[:1]:
	print('\nFor ' + video)
	soup = BeautifulSoup(requests.get(video).text,'lxml')
	tagsList.extend([ i.string  for i in soup.find_all('a','video-tag') ])
	print(len(tagsList))
	
frequency = {}
for i in tagsList:
	try:
		frequency[i] += 1
	except KeyError:
		frequency[i] = 1

import json

with open('result.json','w') as file:
	json.dump(frequency,file)