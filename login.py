 #coding=utf-8
from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup
from urllib2 import HTTPError
import httplib
import re
import requests
import pymssql 
import exceptions

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
   html=urllib2.urlopen(pageurl)
 except:
    return 0
 
 else:
  pcharset=re.compile(r'charset=.{0,6}')
  match=re.findall(pcharset,html)
  if(match[0]=="charset=gb2312"):
   html=html.decode("gbk")
  try:
   bsobj=BeautifulSoup(cont)
  except: 
   return 0
  else:
   pattern=re.compile(r'\.')
   key=re.split(pattern,pageurl)[1]
   result=bsobj.findAll("a",href=re.compile("^(http://).*(com|cn|com/|cn/|com.cn|com.cn/)$"))
   opdb(pageurl[:20],bsobj.title)	
   if result==[]:
     return 0
   else:
     for tt in result:
       set_t.append(tt.attrs['href'])
     clear(key,set_t)
  return 1
  
def opdb(oh,ot):  
 conn = pymssql.connect(host="PC-201405271757",user="sa", password="123456",database="URLSET",charset='utf8')   #初始化数据库
 cur = conn.cursor()  
 sql="INSERT INTO collections VALUES('%s','%s')"%(oh,ot)
 cur.execute(sql)	
 conn.commit()
 cur.close()
 conn.close()	


#**************************main author=....freeze************************#
inital="http://www.4399.com"
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
 
