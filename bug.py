import urllib2
f=open('f:\\baidu.html','w')
re=urllib2.urlopen("http://www.baidu.com")
content=re.read()
f.write(content)