#! /usr/bin/env python
#coding=utf-8
import re
import sys
import json
import urllib
import urllib2
import cookielib
import jsbeautifier
import execjs




def main():
	clipUrl = 'http://qdrama.org/huang-feng-prison/3.html'
	cj = cookielib.CookieJar()
	handler =urllib2.HTTPCookieProcessor(cj)
	opener =  urllib2.build_opener(handler)
	opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'),
	('Upgrade-Insecure-Requests','1'),
	('Host','qdrama.org')
	]
	page_buf = opener.open(clipUrl).read()
getp(1,0,"([^\"]+)","([^\"]+)"
	rawresult = jsbeautifier.beautify(page_buf)
	result = "'''"+rawresult+"'''"
	srere = result.decode('unicode-escape')
	print srere
	#ctx = execjs.compile(result)
	#ctx.call('getp',1,0,'nhayH3DfGKX38kTpg9VKCodYJDMH-eKlCSacjPQRLCied6EO-be7dZ5FcgSTCZft9OhVdO22aMtiAK01bTelo-SsbDhv_q89qHzh8SubzmNheoLk5VOGVM27gQqgt3ypjiTtUQLVveA2ey8SzidlT3uxumuxMXNgBh-G4626iM5v_DRp5Nb0WNtXAox7caVkVYjzUe3e6QOEsk4po-dwSnIP442LCYZpiOtt0CZ','XXtnwBKc6F4yK60pgdr8JYDmRr2vpL4W0rJ-QtGjMDzmKBd8XoODMtyIV01rvIE2UtdOFRQCdkCdo1vM7G80qTHurDNLs1FkhGdeCnixZxdKK9bEQ26ki_LcU86szq0yVtoIXdAFfdBn4RAix-Rm95APAmS3crtXGsTRSeX70fvDp_bKrfnA6q2nCicDDefI1MOMlBFbGD78rSrYQJCpehKk2WM6Ihi9CWHjR92fWbj8F_R1lNFhO--GYWHXuR6hIiNIs98NCwYDsj3Cc7Xj_hUrwTL6uXiq4YRX0w8XVl_T_Dw_zEBlX6t6qdkMbVypievVuTuEUJxgE-8Z4wqxl7CFgZa3_ukYRL_yl4gw-1gu-qIUu4Irl25BcBkKn-rRXTuxYG8pC11rs0I')
	
	

if __name__=="__main__":
	main()
