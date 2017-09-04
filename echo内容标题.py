 #coding=utf-8
import pymssql 
import re
import requests
from bs4 import BeautifulSoup
import chardet
import urllib2

def dbwrite(u,t):
 nect= pymssql.connect(host="PC-201405271757",user="sa", password="123456",database="URLSET",charset='utf8')   #初始化数据库
 curr= nect.cursor()
 if(type(t)==unicode):
  t=t.encode('utf-8')
 sql="INSERT INTO ut VALUES('%s','%s')"%(u,t)
 try:
  curr.execute(sql)
 except:
  return 0
 else:
  nect.commit()
  curr.close()
  nect.close()
  return 1
 
 
def gett(url):
 try:
  content=urllib2.urlopen(url,timeout=20).read()
 except:
  return 0
 else:
  code=chardet.detect(content)['encoding']
  if(code=='GB2312'):
   try:
    changecont=content.decode('GBK')
   except:
    return 0
   else:
    match=re.findall(pattern,changecont)
    if(match==[]):
     return 0
    else:
     for it in match:
      k=dbwrite(url,it)
      if(k==0):
	  return 0
	 
  else:
   match=re.findall(pattern,content)
   if(match==[]):
    return 0
   else:
    for it in match:
     k=dbwrite(url,it)
     if(k==0):
	  return 0
   
   
conn = pymssql.connect(host="PC-201405271757",user="sa", password="123456",database="URLSET",charset='utf8')   #初始化数据库
cur = conn.cursor()  
sql="SELECT url FROM collections"
cur.execute(sql)
rows=cur.fetchall() 
conn.commit()
cur.close()
conn.close()
pattern=re.compile(r'<title>(.*?)</title>')

i=0

for fuck in rows:
 temp=str(fuck)  #change tuple element to string
 goin=temp[3:-3]
 flag=gett(goin)
 if(flag==0):
  continue
 print '%d success' % i
 i=i+1
 #i=i+1
