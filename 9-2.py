#!/usr/bin/python
L = ['adam','lisa','bart','paul']
n = range(1,len(L)+1)
l = zip(L,n)
for index, name in l:
	print index,'-',name
