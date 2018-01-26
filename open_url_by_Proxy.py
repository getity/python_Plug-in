#! /usr/bin/env python
#coding=utf-8
import re
import urllib2
import requests
proxies = {
  "http": "http://172.0.240.10:4130",
  "https": "http://172.0.240.10:4130",
}

proxy = urllib2.ProxyHandler({
  "http": "http://172.0.240.10:4130",
  "https": "http://172.0.240.10:4130",
})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
print urllib2.urlopen('http://www.google.com').read()
print '^^^^^^^^^^^^^^^'
print urllib2.urlopen('https://www.google.com').read()





	



	
	
