#!/usr/bin/python2.6
#-*-coding:utf-8-*-
#mooc test 9-4 迭代dict的key和valuev
d = {'adam':95,'lisa':85,'bart':59,'paul':74}
l = d.items()
sum = 0.0
for k ,v in l:
	sum = sum + v 
	print k,':',v
print 'average',':',sum/len(l)
