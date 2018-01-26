#! /usr/bin/env python
#coding=utf-8
import re
import sys
import json
import urllib
import urllib2
import cookielib

def decodeSort(d):
	key = 'ttrandomkeyqdramaorg'
	strr=''
	for i in range(0, len(d)):
		if (0 == i or 0 == (i % (len(key) + 1))):
			strr = strr + d[i:(i+1)]
	return strr[::-1]


def process(param_dic):
	clipUrl = ''
	res = dict()
	clipUrl = param_dic["hostingurl"]
	cj = cookielib.CookieJar()
	handler =urllib2.HTTPCookieProcessor(cj)
	opener =  urllib2.build_opener(handler)
	opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'),
	('Upgrade-Insecure-Requests','1'),
	('Host','qdrama.org')
	]
	page_buf = opener.open(clipUrl).read()
	pattern = 'getp\(1,0,"([^\"]+)","([^\"]+)"'
	strc = re.search(pattern,page_buf).group(1)
	stra = re.search(pattern,page_buf).group(2)
	dc = decodeSort(strc)
	da = decodeSort(stra)
	result = ''
	if dc == 'dailymotion' :
		result = 'http://www.dailymotion.com/video/'+da
	else:
		result = 'http://drama6.com/v6/?ref='+da
	res['service_result']= result
	return json.dumps(res)

if __name__=="__main__":
	params = sys.stdin.readline()
	param_dic = json.loads(params)
	result = process( param_dic )
	sys.stdout.write(result)
