# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import chardet
import pymssql
import urllib
import os
url="http://www.zhihu.com"  #r
url1="http://www.qq.com"   #f
url2="http://www.4399.com"  #f
url3="http://www.10339.com" #r
 
#r=requests.get(url)
#print r.url
#print r.encoding
#print r.text.encode('gbk')
f=open("f:\\ceshi.txt","w")
def dbwrite(u,t):
 nect= pymssql.connect(host="PC-201405271757",user="sa", password="123456",database="URLSET",charset='utf8')   #初始化数据库
 curr= nect.cursor()
 if(type(t)==unicode):
  t=t.encode('utf-8')
 sql="INSERT INTO ut VALUES('%s','%s')"%(u,t)
 curr.execute(sql).
 nect.commit()
 curr.close()
 nect.close()
 
content=urllib.urlopen(url3).read()
pattern=re.compile(r'<title>(.*?)</title>')
code=chardet.detect(content)['encoding']
print code

if(code=='GB2312'):
 print 'y'
 changecont=content.decode('GBK')
 match=re.findall(pattern,changecont)
 if(match!=[]):
  for it in match:
   f.write(it)
   dbwrite(url2,it)
   f.close()
   os.system("f:\\ceshi.txt")
else:
 match=re.findall(pattern,content)
 if(match!=[]):
  for it in match:
   f.write(it)
   dbwrite(url2,it)
   f.close()
   os.system("f:\\ceshi.txt")
 