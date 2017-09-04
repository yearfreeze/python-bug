# -*- coding: utf-8 -*-
import urllib2
import urllib
import cookielib
data={"email":"a747241658@qq.com","password":"qq1995124"}
post_data=urllib.urlencode(data )
cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
req=urllib2.Request("http://www.renren.com/PLogin.do",post_data)#PLogin
content=opener.open(req)

f=open('f:\\renren111.html','w')
f.write(content.read())
#print content.read()