#coding:utf-8
import  re  #正则表达式

p = re.compile(r'\d+')
print p.findall('one123two234three345four456')

info = '<a href="http://www.baidu.com">百度</a>'
pattern1 = '<a href="(.*)">(.*)</a>'

info='<a href="/users/11243191/" target="_blank" title="呢称已被注册"><h2>呢称已被注册</h2></a>'
pattern1 = '<a href=".*">(.*)</a>'

items = re.findall(pattern1,info)
for item in items:
    print item

#re.I(忽略大小写)、re.L(依赖locale)、re.M(多行模式)、re.S(.匹配所有字符)、re.U(依赖Unicode)、re.X(详细模式)