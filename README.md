# Python Scrapy

An simple crawler/scrapy that can download all images and video of the given Tumblr account, based on the Tumblr url input. The download stream will store in a folder under same directory as the running application. 
The key point for this application is knowing the HTML structure of the targeted Tumblr blog, for example, is it controlled by the scroll or pagination? What are the tag id for those? How can we judge that there is no more page? How to filter the original image and thumbnail?

## Requiremetns
*Python3.3+
*Works on Windows

## Install and Use
Just click "clone" or "download" in this page, and open the Python file tumblr_crawler.py

## Update
* rewrite the functions, make it suits more Tumblr blog structure, add function of downloading video.

## Reference libraries/APIs
* BeautifulSoup
* re
* requests
* htmlParse
