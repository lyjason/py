#!/usr/bin/python
#-*-coding:utf-8-*-
#带验证的系统登录脚本

print 'Hello! This is Jason`s login system.'
name = raw_input("Identify yourself: ")
#接收用户输入

usr=['jason','xiaowu','dahai','saoren']
#规定可用用户名

for i in usr :
  if name == i :
    print 'Welcom! ',i
#用 i 来输出usr列表里的字符，给if语句判断，如果成立，执行print。如果不成立，继续提出usr字符串继续判断。
