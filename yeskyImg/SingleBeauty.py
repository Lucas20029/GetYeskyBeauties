#coding:utf-8
import  urllib
import  urllib2
import  re  #正则表达式

def GetContentByURL(url, IsUtf8):
    try:
        request = urllib2.Request(url)
        response=urllib2.urlopen(request)
        content = response.read()
        if (IsUtf8==True):
            return  content.decode('utf-8')
        return content
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print "ex with code"
            print e.code
        if hasattr(e,"reason"):
            print "ex with code"
            print  e.reason

#打开一个人的详情页后，获取这个人所有的图片链接地址
def FindLinksInSingle(url):
    content= GetContentByURL(url,False)
    pattern = re.compile('<div id="scroll".*?<ul>(.*?)</ul>', re.S) #定位UL下面的li
    items = re.findall(pattern, content)
    pattern = re.compile('<a href="(.*?)" target', re.S)  #取出每个li里面的链接
    links = re.findall(pattern, items[0])
    return links

#FindLinksInSingle("http://pic.yesky.com/293/108578293.shtml")
#从一个图片的详情页里面，获取该页的大图
def GetLargeImageOfPage(url):
    content = GetContentByURL(url,False)
    pattern =re.compile('<div class="l_effect_img_mid".*?<img src="(.*?)" alt',re.S)
    imgLink =re.findall(pattern,content)[0]
    return imgLink
#保存到本地
def SaveImgUrlToFile(imgUrl, newfilePath):
    urllib.urlretrieve(imgUrl,newfilePath)

SaveImgUrlToFile("http://dynamic-image.yesky.com/740x-/uploadImages/2017/048/41/N0C382VD858Z_800x1200.jpg","E:/SpyImg/1.jpg")