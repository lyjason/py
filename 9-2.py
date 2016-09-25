#!/usr/bin/python2.62.6
#-*-coding:utf-8-*-
#课堂训练
#zip命令、range命令
L = ['adam','lisa','bart','paul']
n = range(1,len(L)+1)
l = zip(L,n)
for index, name in l:
	print index,'-',name
