import re
from HTMLParser import HTMLParser
import requests
username='13030140104'
password='04003X'
xd='http://ids.xidian.edu.cn/authserver/login?service=http%3A%2F%2Fjwxt.xidian.edu.cn%2Fcaslogin.jsp'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
s = requests.session()
r = s.get(xd)
cont=r.text.encode('utf-8') 
#print cont
pattern=re.compile(r'<input type="hidden" name="lt" value=(.*)/>')# <input type="hidden" name="lt" value="(.*?)"/>
match=re.findall(pattern,cont)
for it in match:
 print it
	
Lt=it[1:-2]
print Lt

login_data={'username':username,'password':password,'lt':Lt,'execution':'e1s1','_evenId':'submit','rmShown':'1'}
print login_data
t = s.post('http://jwxt.xidian.edu.cn/caslogin.jsp', login_data, headers)#log in xd
print t.text.encode('utf-8') 
    
 
