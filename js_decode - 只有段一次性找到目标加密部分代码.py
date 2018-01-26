#! /usr/bin/env python
#coding=utf-8
import json
import sys
import urllib2
import re
import string
digs = string.digits + string.letters

def int2base(x, base):
  if x < 0: sign = -1
  elif x == 0: return digs[0]
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

def unpack(p, a, c, k, e=None, d=None):
    ''' unpack
    Unpacker for the popular Javascript compression algorithm.

    @param  p  template code
    @param  a  radix for variables in p
    @param  c  number of variables in p
    @param  k  list of c variable substitutions
    @param  e  not used
    @param  d  not used
    @return p  decompressed string
    '''
    # Paul Koppen, 2011
    for i in xrange(c-1,-1,-1):
        if k[i]:
            p = re.sub('\\b'+int2base(i,a)+'\\b', k[i], p)
    return p


#pagebuf=urllib2.urlopen('http://dropvideo.com/embed/DHSYATGCLS/').read();

#pattern="eval\(function.*"
#pattern="<script type='text/javascript'>eval\(function.*\s</script>"
#js_content=re.search(pattern,pagebuf);

#print js_content.group();
#s=js_content.group()
#result = eval('unpack' + s[s.find('}(')+1:-1])

#print result

def main():
    res={}
    input = sys.stdin.read()
#    fo=open("pagebuf.txt","r+")
#    page_buf=fo.read()
    js=json.loads(input)
    page_buf=js['pagecontent']
    pattern="(eval\(function[^<]*?\)\)\))\s*</script"
#pattern='id="flowplayer[^^]*(eval\(function.*?}\)\))'
#    s=re.search(pattern,page_buf).group()
    s=re.search(pattern,page_buf).group(1)
    result = eval('unpack' + s[s.find('}(')+1:-1])
#    print result
    res['field']=result
    sys.stdout.write(json.dumps(res))

if __name__=="__main__":
    main()
