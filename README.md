# Python Scrapy

An simple crawler/scrapy that can download all images and video of the given Tumblr account, based on the Tumblr url input. The download stream will store in a folder under same directory as the running application. 
The key point for this application is knowing the HTML structure of the targeted Tumblr blog, for example, is it controlled by the scroll or pagination? What are the tag id for those? How can we judge that there is no more page? How to filter the original image and thumbnail?

## Requiremetns
* You need to download BeautifulSoup4 and lxml to successfully run this program.  
Ex. run this in CMD to download: "pip install lxml"  
* Python 3.3+  
* BeautifulSoup 4.2  
* Works on Windows  

## Install and Use
Just click "clone" or "download" in this page, and open the Python file tumblr_crawler.py  

## Update
* rewrite the functions, make it suits more Tumblr blog structure, add function of downloading video.  


## Warning
This program may not work due to different BeautifulSoup version  

## Reference libraries/APIs
* BeautifulSoup  
* re  
* requests  
* htmlParse  

## Display
The program should run like this(in Sublime command):
![alt text](https://github.com/Ros1n/python_scrapy/blob/master/crawler_display.PNG)

