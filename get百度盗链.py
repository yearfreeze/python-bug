#-*- coding:gbk-*-
import urllib
from urllib import urlopen
import os
import argparse
import re
import requests
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()

c=args.echo
d=c.decode('gbk').encode('utf-8')
url='http://www.baidu.com/baidu?tn=monline_3_dg&ie=utf-8&wd='+d


page=urlopen(url)
html=page.read()
bsobj=BeautifulSoup(html)

fucks =bsobj.findAll("a",{"href":re.compile("http://www.baidu.com/link.*")})
for fuck in fucks:
 tt=fuck.attrs['href']
 #print tt
 r=requests.get(tt)
 print r.url


#print r.headers #get response head
#print r.status_code 
#print r.encoding
#print r.url #get the real url address 



