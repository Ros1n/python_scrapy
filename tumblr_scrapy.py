import re
import requests
import os
from bs4 import BeautifulSoup

class tumblr_scrapy:
	def __init__(self):
		self.count = 0

	def convert_html_data(self, url):
		if re.match(r'^http://[0-9a-zA-Z\_\.\-\/]+tumblr\.com/$', url):
			pass
		else:
			url = input('the url is invalid. Type a new one: ')
			self.grab_img(url)
		content = requests.get(url).content #here equals to urllib2.urlopen(url)
		soup = BeautifulSoup(content, 'lxml')
		title = soup.title.string
		print('the tumblr account is: ' + title)
		if not os.path.exists(title):
			os.makedirs(title)
		cur_dir = os.getcwd()
		os.chdir(cur_dir+'/'+title)
		pages = self.collect_page(soup)
		for i in range(1, int(pages)):
			self.grab_img(soup)
		print('finish download')

	def collect_page(self, soup):
		if soup.find('pagination'):
			total_pages = soup.find(id='pagination').a['data-total-pages']
		else:
			total_pages = 2
		return total_pages

	#main method
	def grab_img(self, soup):
		count = 0
		#img_src = soup.section.section.div.find_all('img')
		img_src = soup.find_all('img')
		#os.path.join(os.path, title)
		for line in img_src:
			line = line['src']
			print(line)
			try:
				pic = requests.get(line, timeout=10)
			except requests.exceptions.ConnectionError:
				print('Error: the image cannot been download')
				continue
			string = 'pictures'+str(self.count)+'.jpg'
			fp = open(string, 'wb')
			fp.write(pic.content)
			fp.close()
			self.count += 1

if __name__ == '__main__':
	obj = tumblr_scrapy()
	url = input('url: ')
	#url = 'http://asuka-persona.tumblr.com/'
	obj.convert_html_data(url)
