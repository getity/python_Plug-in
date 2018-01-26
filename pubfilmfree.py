#!/usr/bin/env python
#coding:utf-8

import os
import re 
import sys
import json
import string
import urllib
import urllib2


def process( param_dic ):
    res = dict()
    clipUrl = param_dic["hostingurl"]
    opener   =  urllib2.build_opener()
    opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'),
    ('Host','pubfilmfree.com')]
    data = opener.open(clipUrl).read()
    phimid=int(re.search('"phimid"\s*value="([^"]+)',data).group(1))
    server=int(re.search('"server"\s*value="([^"]+)',data).group(1))
    epname=int(re.search('"epname"\s*value="([^"]+)',data).group(1))
    test_data = {'ipplugins':1,'ip_film':phimid,'ip_server':server,'ip_name':epname}
    test_data_urlencode = urllib.urlencode(test_data)
    requrl = 'http://pubfilmfree.com/ip.file/swf/plugins/ipplugins.php'
    req = urllib2.Request(url = requrl,data =test_data_urlencode)
    req.add_header('Host', 'pubfilmfree.com')	
    req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0')
    res_data = urllib2.urlopen(req)
    page_buf = res_data.read()
    jsonCont = json.loads(page_buf)
    zurl = jsonCont.get('s')
    aurl = str(zurl)
    burl = 'http://pubfilmfree.com/ip.file/swf/ipplayer/ipplayer.php?u='+aurl+'&w=100%&h=500&s=4&n=0'
    data2 = opener.open(burl).read()
    jsonCont = json.loads(data2)
    curl=jsonCont.get('data')
    strr = str(curl)
    resss=re.search('files\':\s*u\'([^\']+)',strr)
    if resss:
        res["service_result"]= resss.group(1)
    else:
        res["service_result"]= 'https:'+strr
    result = json.dumps(res)
    return result
    
if __name__ == '__main__':
    params = sys.stdin.readline()
    #参数是一个字符串一般转换为map
    param_dic = json.loads(params)
    result = process( param_dic )
    print result #只能print需要的东西

	
