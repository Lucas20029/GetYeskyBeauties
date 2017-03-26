#coding=utf-8
import bs4
from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie  --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,"lxml")

#打印html的头标签
def PrintSomeTags():
    print "Soup head:  " + str( soup.head )
    print "Soup title: " + str( soup.title )
    print "The 1st a:  " + str( soup.a )
    print "The 1st p:  " + str( soup.p )

def FindAllLinks():
    links = soup.findAll("a")#获取soap里面所有的a标签
    print  "All the links are bellow: "
    for link in links:
        print  link
def UseLinkAttr():
    print "The link attributes are bellow: "
    print soup.a.get("id")
    print soup.a["href"]
    soup.a["href"]= "http://www.baidu.com"
    print soup.a["href"]
    del soup.a["href"]
def GetText():
    print "a inner text and attr"
    print soup.a.string  #a里面的内容
    print type(soup.a)  # a的类型：是标签
    print type(soup.a.string)  #a.string的类型是注释  <!--Elsie-->
    if type(soup.a.string)==bs4.element.Comment:
        print "The inner text is comment"
    else:
        print "The inner text is not comment"

def GetContent():
    print soup.head.contents
    print soup.body.contents[1]
def GetChildren():
    bodyEles = soup.body.children
    print "The Children elements are bellow:"
    for ele in bodyEles:
        print ele

#PrintSomeTags()
#FindAllLinks()
#UseLinkAttr()
#GetText()
#GetContent()
GetChildren()
#aList = soup.findAll("a")
#for aitem in aList:
    #print  aitem.attrs