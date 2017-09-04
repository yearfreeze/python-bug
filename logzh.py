#encoding=utf-8
from HTMLParser import HTMLParser
import requests
import os

if __name__ == "__main__":
    phonenum='a747241658@qq.com'
    pwd='qq1995124'
    mainURL='http://www.zhihu.com'
    loginURL='http://www.zhihu.com/login/email'#http://www.zhihu.com/login/email
    
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'}
    
    s = requests.session()
    r = s.get(mainURL)
    print r.cookies     
    
    login_data = {'_xsrf':r.cookies['_xsrf'], 'email':phonenum, 'password':pwd, 'rememberme':'y'}
    t = s.post(loginURL, login_data, headers)
    print t.text       

    t = s.get(mainURL,verify=False)
    #print  t.text.encode('utf-8')
    f = open('zhihu_test.html','w')
    f.write(t.text.encode('utf-8'))
    os.system("f:\\top.html")
	

	
