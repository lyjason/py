#!/usr/bin/python

def a(L):
	w=[]
	for x in L:
		x=x**2
		w.append(x)
	y=sum(w)
	return y
print a([2,3,4,5,6])
print a([-2,4,4,6,0])
