import urllib
import urllib2

#Get方法请求页面。拼接查询字符串

#简单请求URL的HTML
def GetHtmlWithoutHead(urlstr):
    response1=urllib2.urlopen(urlstr)
    return response1.read()
#封装成Request对象
def GetBaiduHtml1():
    request1 =urllib2.Request("http://www.baidu.com")
    response2=urllib2.urlopen(request1)
    return response2.read()
#Get方法，拼接URL查询字符串
def GetRequestWithParam():
    values ={}
    values["username"] = "52547189@qq.com"
    values["password"] ="123456"
    data=urllib.urlencode(values)
    url = "http://www.csdn.net"
    fullUrl = url+"?"+data
    print  fullUrl

print GetHtmlWithoutHead("https://www.zhihu.com/")
