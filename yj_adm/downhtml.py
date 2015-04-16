#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import http.cookiejar
from html.parser import HTMLParser 
url1= "http://adm.91yaojiang.com/Login.aspx"
url2= "http://adm.91yaojiang.com/Malls/List.aspx"
#url = 'http://www.baidu.com/'
def down_web(url1,url2):
	params={'UserName':'yuying','login_Password':'asdfg991134',}
	webCookie=http.cookiejar.CookieJar()
	openner = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(webCookie))
	webRequest=openner.open(url1,urllib.parse.urlencode(params).encode())
	webRequest = openner.open(url2) 
	htmlData=webRequest.read()
	#print (htmlData)
	#pre_url={}
	#pre_url['word']='abc'
	#full_url="http://www.baidu.com/s?"+urllib.parse.urlencode(pre_url)
	#data = urllib.request.urlopen(url).read()
	#data = data.decode('UTF-8','ignore').encode('UTF-8','ignore')
	save_name='w'+'.html'
	with open(save_name,'wb') as file:
		file.write(htmlData)
	file.close()

down_web(url1,url2)


