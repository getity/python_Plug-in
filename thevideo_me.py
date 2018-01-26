#!/usr/bin/env python
# coding=utf8

import os
import re 
import sys
import json
import string
import urllib
import urllib2 
import hashlib
import getopt
import traceback
import cookielib
import random
import tempfile
import time
import string
digs = string.digits + string.letters

reload(sys)
sys.setdefaultencoding('utf-8') 





def download_page(url, proxy = None, referer = None):
    page_buf = ''
    i = 0
    for i in range(3):
        try:
            if proxy:
              handlers = [urllib2.ProxyHandler({'http': 'http://%s/' % proxy})]
              opener =  urllib2.build_opener(*handlers)
            else:
              opener   =  urllib2.build_opener()
              method   =  urllib2.Request(url)
            if referer:
              method.add_header('Referer', referer)
            method.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36')
            method.add_header('Accept-Language', 'en-US,en;q=0.5')
            result   =  opener.open(method, timeout=10)
            page_buf =  result.read()
            return page_buf
        except urllib2.URLError, reason:
            return str(reason)
        except Exception, reason:
            if i == 2:
                raise Exception(reason)


def get_regex_data(regex, buf):
  group = re.search(regex, buf)
  if group:
    return group.group()
  else:
    return ''



def main():
    res={}

    input = sys.stdin.readline()
    jsonCont = json.loads(input)
    clipUrl = jsonCont.get('hostingurl')
    proxy =   jsonCont.get('proxy')
    key=re.search('me/(\w+)',clipUrl).group(1)
    data=download_page(clipUrl,proxy)
    cj = cookielib.CookieJar()
    if proxy:
        handlers = [urllib2.ProxyHandler({'http': 'http://%s/' % proxy,'https': 'http://%s/' % proxy}),urllib2.HTTPCookieProcessor(cj)]
        opener =  urllib2.build_opener(*handlers)
    else:
        opener   =  urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'),
                         ('Referer',clipUrl),
                         ('Host','thevideo.me')
                         ]
    _vhash=re.search('_vhash\', value: \'(.*?)\'',data).group(1)
    gfk=re.search('gfk\', value: \'(.*?)\'',data).group(1)
    fname=re.search('fname" value="(.*?)"',data).group(1)
    hash_=re.search('hash" value="(.*?)"',data).group(1)
    post_data='_vhash='+str(_vhash)+'&gfk='+str(gfk)+'&op=download1&usr_login=&id='+str(key)+'&fname='+str(fname)+'&referer='+str(clipUrl)+'&hash='+hash_+'&inhu=foff&imhuman='
    #print str(cj)
    op=opener.open(clipUrl,post_data).read()

    lets_play_a_game = re.search('lets_play_a_game=\'(.*?)\'',op).group(1)
     
    js_url ='https://thevideo.me/vsign/player/'+lets_play_a_game
    js_data = opener.open(js_url).read()
    #print js_data
    result=re.search('(eval\(function[\d\D]*?\)\))',js_data).group(1)



    res['field']=result
    sys.stdout.write(json.dumps(res))


if __name__ == '__main__':
    main()
