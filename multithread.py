 #coding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup
from urllib2 import HTTPError
import httplib
import re
import threading
import pymssql 

lock=threading.Lock()
tlock=threading.Lock()
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
    safechange(item)

def safechange(data):
  lock.acquire()
  total.append(data)
  lock.release()
  
def getlinks(pageurl):
 set_t=[]
 try:
    html=urllib2.urlopen(pageurl)
 except:
    return 0
 
 else:
  try:
   bsobj=BeautifulSoup(html)
  except: #unicode decode error
   return 0
  else:
   pattern=re.compile(r'\.')
   otitle=unicode(bsobj.head.title).encode("utf-8")[7:15] 
   key=re.split(pattern,pageurl)[1]
   result=bsobj.findAll("a",href=re.compile("^(http://).*(com|cn|com/|cn/|com.cn|com.cn/)$"))
   opdb(pageurl,otitle) 
   if result==[]:
    return 0
   else:
    for tt in result:
      set_t.append(tt.attrs['href'])
    clear(key,set_t)
  return 1
  
def opdb(oh,ot):
 tlock.acquire()
 conn = pymssql.connect(host="PC-201405271757",user="sa", password="123456",database="URLSET",charset='utf8')   #初始化数据库
 cur = conn.cursor()  
 sql="INSERT INTO collections VALUES('%s','%s')"%(oh,ot)
 cur.execute(sql)
 conn.commit()
 cur.close()
 conn.close()	
 tlock.acquire()
 
def subthread(n): #sub thread do
  while(len(total)>len(cost)):
   if(len(total)>n):
    getlinks(total[n])
    print total[n]
    n=n+5
    cost.append(total[n])
	 
#**************************main author=....freeze************************#
inital="http://www.4399.com"
global total
total=[]
global cost
cost=[]



getlinks(inital)
if(len(total)==0):
 print '1'

t1=threading.Thread(target=subthread,name='1',args=(0,))
t2=threading.Thread(target=subthread,name='2',args=(1,))
t3=threading.Thread(target=subthread,name='3',args=(2,))
t4=threading.Thread(target=subthread,name='4',args=(3,))
t5=threading.Thread(target=subthread,name='5',args=(4,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

 
 
	
