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

def getHostingURL(self):
    url = ''
    url = param_dic["hostingurl"]
    return url
	
def processy(rawUrl):		
	cj = cookielib.CookieJar()
	handler =urllib2.HTTPCookieProcessor(cj)
	opener1 =  urllib2.build_opener(handler)
	opener1.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'),
	('Upgrade-Insecure-Requests','1'),
	('Host','qdrama.org')
	]
	
	#取得cx
	page_buf1 = opener1.open('http://qdrama.org/').read()
	cx = re.search('var\s*cx\s*=\s*\'([^\']+)',page_buf1).group(1)
	getcx = re.search('gcse\.src\s*=\s*\'([^\']+)',page_buf1).group(1)
	tokUrl = getcx + cx
	
	#proxy = urllib2.ProxyHandler({
	#"http": "http://172.0.240.10:41282",
	#"https": "http://172.0.240.10:41282",
	#})
	#opener = urllib2.build_opener(proxy)
	opener = urllib2.build_opener()
	urllib2.install_opener(opener)
	
	page_buf2 = urllib2.urlopen(tokUrl).read()
	cse_tok = re.search('\"cse_token\"\s*:\s*\"([^\"]+)',page_buf2).group(1)

	listPurl = []         
	for i in range(0,100,10):
		purl = rawUrl+str(i)+'&cx='+cx+'&cse_tok='+cse_tok
		listPurl.append(purl) 

	listEurl = []
	for x in listPurl:
		page_buf3 = urllib2.urlopen(x).read()
		eurls = re.findall('\"ogUrl\"\s*:\s*"(http://www.qdrama.org/[\w-]+/)',page_buf3)
		if eurls:
			listEurl = listEurl + eurls
	listEurl = list(set(listEurl))

	
	listSurl = []
	for k in listEurl:
		page_buf4 = opener1.open(k).read()
		pattern = '<li><a\s*href="(http://qdrama.org/[\w-]+/\d+\.html)"\s*target="_blank">'
		surls = re.findall(pattern,page_buf4)
		if surls:
			listSurl = listSurl + surls
	
	dict1 = {'youtube':'http://www.youtube.com/embed/',
			'dailymotion':'http://www.dailymotion.com/embed/video/',
			'yktd':'http://video.tudou.com/v/',
			'm3u8':'http://drama6.com/m3u8/?ref=',
			'kuyunbo':'https://cdn.kuyunbo.club/share/',
			'openload':'https://openload.co/embed/',
			'streamango':'https://streamango.com/embed/',
			'vidme':'https://vid.me/e/',
			'video66':'http://video66.org/embed.php?vid=',
			'uploadly':'https://uploadly.com/embed/',
			'vimeo':'http://player.vimeo.com/video/',
			'linetv':'https://tv.line.me/embed/',
			'acfun':'http://cdn.aixifan.com/player/ACFlashPlayer.out.swf?type=page&url=http://www.acfun.tv/v/ac',
			'adrama':'http://drama6.com/v0/?ref=',
			'bdrama':'http://drama6.com/v1/?ref=',
			'cdrama':'http://drama6.com/v2/?ref=',
			'ddrama':'http://drama6.com/v3/?ref=',
			'edrama':'http://drama6.com/v4/?ref=',
			'fdrama':'http://drama6.com/v5/?ref=',
			'gdrama':'http://drama6.com/v6/?ref='
			}
	result = ''
	for j in listSurl:
		page_buf5 = opener1.open(j).read()	
		pattern = 'getp\(1,0,"([^\"]+)","([^\"]+)"'
		strc = re.search(pattern,page_buf5).group(1)
		stra = re.search(pattern,page_buf5).group(2)
		dc = decodeSort(strc)
		da = decodeSort(stra)
		hurl = ''
		if dict1.get(dc) :
			hurl = dict1.get(dc) +da
			result = result + '\''+hurl +'\';'
	result = result[0:-1]
	return result

	
if __name__ == '__main__':
	parms = sys.stdin.readline()
	param_dic = json.loads(parms)
	url = getHostingURL(param_dic)
	ret = processy(url)
	r = {}
	r["service_result"]=ret
	print json.dumps(r)	