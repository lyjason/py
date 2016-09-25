#!/usr/bin/python2.62.6
#-*-coding:utf-8-*-
#课堂训练:一个list的平方和
def a(L):
	w=[]
	for x in L:
		x=x**2
		w.append(x)
	y=sum(w)
	return y
print a([2,3,4,5,6])
print a([-2,4,4,6,0])
