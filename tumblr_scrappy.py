import re
import requests
import os
from bs4 import BeautifulSoup

class tumblr_scrapy:
	def __init__(self):
		html_sample = 'Tumblr'

	def create_dir(self, fileName):
		if not os.path.exists(fileName):
			os.makedirs(fileName)
		cur_dir = os.getcwd()
		os.chdir(cur_dir + '/' + fileName)

	def grab_stream(self, soup, streamName):
		image_format = ('.jpg', '.gif', '.png', '.jpeg', '.bmp')
		for line in soup.find_all(streamName):
			if streamName == 'iframe':
				if '/video/' not in line:
					continue
			stream_str = line.get('src')
			try:
				stream = requests.get(url=stream_str, timeout=10)
			except requests.exceptions.ConnectionError:
				print('Error: the stream cannot been download')
				continue
			if (streamName == 'img' and stream_str.endswith(image_format)):
				stream_name = stream_str.split('/')[-1]
			elif streamName == 'iframe':
				streamName = stream_str.split('tumblr_')[1].split('/')[0] + '.mp4'
			else:
				continue
			if not os.path.isfile(stream_name):
				print('[*] Source %s is downloading...' % stream_name)
				fp = open(stream_name, 'wb')
				fp.write(stream.content)
				fp.close()
			else:
				print('[*] Source %s has been downloaded.' % stream_name)

	def scrapy_work(self, url, page_index):
		print(url + 'page/' + str(page_index))
		content = requests.get(url + 'page/' + str(page_index)).content #here equals to urllib2.urlopen(url)
		soup = BeautifulSoup(content, 'lxml')
		self.grab_stream(soup, 'img')
		self.grab_stream(soup, 'iframe')
		if soup.find("a", attrs={"class": "next", "data-current-page": str(page_index)}) or soup.find("a", attrs={"class": "load-more-icon"}) or soup.find('a', attrs={"href": "/page/" + str(page_index+1)}):
		 #or soup.find("section", attrs={"id": "posts"}).find('a'):  #pagination = soup.find('id', 'pagination')
			self.scrapy_work(url, page_index+1)  #pagination = soup.select("body >  div > #pagination")
		else:
			print('finish download!')


if __name__ == '__main__':
	scrapy = tumblr_scrapy()
	url = input('please enter the url: ')
	#Example: url = 'http://asuka-persona.tumblr.com/'
	while not re.match(r'^http(s)?://[0-9a-zA-Z\_\-\/]+.tumblr\.com/$', url):
		url = input('the url is invalid. Type a new one: ')
	title = url.split('//')[1].split('.tumblr')[0]
	print('the tumblr account is: ' + title)
	scrapy.create_dir(title)
	scrapy.scrapy_work(url, 1)
