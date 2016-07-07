#!/usr/bin/python
#-*-coding:utf-8-*-
#带验证的系统登录脚本

print 'Hello! This is Jason`s login system.'
name = raw_input("Identify yourself: ")
#接收用户输入

usr=['jason','xiaowu','dahai','saoren']
#规定可用用户名

if name in usr :
    print 'Welcom! ',name
else :
    print 'Please check your input!'    
#用in方法判断字符串是否在列表里
