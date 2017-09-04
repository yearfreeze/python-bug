 #coding=utf-8
from urllib import urlopen
import urllib
import urllib2
from bs4 import BeautifulSoup
from urllib2 import HTTPError
import httplib
import re
import pymssql 
import threading

lock=threading.Lock()
#print (bsobj.head.title).encode("gbk")
#清洗函数
def clear(t,l=[]):
 
 p=re.compile(r'\.')
 for item in l:
  flag=1
  if item not in total:
   for ex in re.split(p,item):
    if t in ex:
	 flag=0
	 break
   if(flag==1):
    total.append(item)
  
def getlinks(pageurl):
 set_t=[]
 try:
  page=urlopen(pageurl)
  html=page.read()
 except:
    return 0
 
 else:
  
  try:
   bsobj=BeautifulSoup(html)
  except: #unicode decode error
   return 0
  else:
   pattern=re.compile(r'\.')
   #otitle=bsobj.head.title
   key=re.split(pattern,pageurl)[1]
   result=bsobj.findAll("a",href=re.compile("^(http://).*(com|cn|com/|cn/|com.cn|com.cn/)$"))
   opdb(pageurl) #url title入数据库
   if result==[]:
    return 0
   else:
    for tt in result:
      set_t.append(tt.attrs['href'])
    clear(key,set_t)
    page.close()
  return 1
  
def opdb(oh):  
 conn = pymssql.connect(host="PC-201405271757",user="sa", password="123456",database="URLSET",charset='utf8')   #初始化数据库
 cur = conn.cursor()  
 sql="INSERT INTO collections(url) VALUES('%s')"%(oh)
 cur.execute(sql)	
 conn.commit()
 cur.close()
 conn.close()	

	 
#**************************main author=....freeze************************#
inital="https://www.sogou.com"
global total
total=[]
getlinks(inital)
if(len(total)==0):
 print '1'


while(total!=[]):
 mark=getlinks(total[0])
 if(mark==0):
  del total[0]
  continue
 else:
  print total[0]
  del total[0]
