#coding:utf-8
import  urllib
import  urllib2
import  re  #正则表达式


page =1
url="http://www.qiushibaike.com/hot/page"+str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request =urllib2.Request(url, headers=headers)
    response=urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author.*?>.*?<a.*?<h2>(.*?)</h2>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        print item
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print "ex with code"
        print e.code
    if hasattr(e,"reason"):
        print "ex with code"
        print  e.reason
