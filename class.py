#!/usr/bin/python
#-*-coding:utf-8-*-
#51CTO课程学习练习
import random
answer = random.randint(0,10)
print('****************jason****************')
num=input('随便输入一个数字来试试运气：')
num=int(num)
i=3;
while i!=0  :
	if num == answer :
		print('你猜对了，好厉害')
		break
	else:
		if num>answer :
			print('不好，大了。')
		else:
			print('哎，小了。')
	i=i-1
	if i!=0 :	
		num=input('请重新输入一个值：')
		num=int(num)
	else :
		print('尝试次数已耗尽')
print('到此结束')
