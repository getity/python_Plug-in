#!/usr/bin/env python
# coding=utf8

import urllib2 
import re 
import sys
import json
import time
import os
import traceback
import random
import tempfile
import time
import urllib

def get_regex_data(regex, buf):
    group = re.search(regex, buf)
    if group:
        return group.groups()[0]
    else:
        return ''

def download_page(url, proxy = None, referer = None):
    page_buf = ''
    time.sleep(2)
    try:
        if proxy:
            handlers = [urllib2.ProxyHandler({'http': 'http://%s/' % proxy})]
            opener =  urllib2.build_opener(*handlers)
        else:
            opener   =  urllib2.build_opener()

        method   =  urllib2.Request(url)
        if referer:
            method.add_header('referer', referer)
        method.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0')
        #method.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        #method.add_header('Accept-Language', 'en-us,en;q=0.5')
        #method.add_header('Accept-Encoding', 'gzip, deflate')
        result   =  opener.open(method, timeout=100)
        page_buf =  result.read()
        return page_buf
    except urllib2.URLError, reason:
        return str(reason)
    except Exception, reason:
        raise Exception(reason)


def main():
    res     = dict()
    status  = ""
    text    = ""
    error   = ""
    redirect_url  = ""

    try:
        input     =   sys.stdin.read()
        jsonCont  =   json.loads(input)
        strkeyid =   jsonCont.get('hostInfo').get('keyid')
        video_url = 'https://yespornplease.com/view/'+strkeyid
        proxy = jsonCont.get('proxy')
        #print video_url
        page_buf = download_page(video_url,proxy)
        b_url=re.search('iframe\s*src="([^\"]+)"',page_buf).group(1)
        s_url = "https:"+b_url
        page_buf2 = download_page(s_url,proxy)		
        if  "Can't find the resource you are looking for" in page_buf2:
            status = 2008
        text = page_buf2

    except:
        error = traceback.format_exc()

    finally:
        res['error']  = error
        res['text']   = text
        res['status'] = status
        res['redirect_url'] = redirect_url
        sys.stdout.write(json.dumps(res))

if __name__ == '__main__':
    main()

