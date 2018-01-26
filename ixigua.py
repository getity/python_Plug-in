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
	#clipUrl = 'https://www.ixigua.com/a6504848610490843662/'
	opener   =  urllib2.build_opener()
	opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'),
	('Host','www.ixigua.com')]
	data = opener.open(clipUrl).read()
	clie_title = re.search('<title>([^\']*)</title>',data).group(1)
	poster = re.search('name:\s*\'([^\']*)\',\s*videoPlayCount',data).group(1)
	poster_url = re.search('mediaUrl:\s*\'([^\']*)\'',data).group(1)
	view_count= re.search('videoPlayCount:\s*(\d+)',data).group(1)
	
	field='"clie_title":"%s";"poster":"%s";"poster_url":"%s";"view_count":"%s"'%(clie_title,poster,poster_url,view_count)
	res['field'] = field
	result = json.dumps(res)
	return result
    
if __name__ == '__main__':
    params = sys.stdin.readline()
    #参数是一个字符串一般转换为map
    param_dic = json.loads(params)
    result = process( param_dic )
    sys.stdout.write(result)

	
