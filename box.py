#!/usr/bin/python2.6
#-*- coding:utf-8 -*-

#以正确的宽度在居中的“盒子”内打印一个句子
#注意：整数除法运算符（ // ）只能用在Python2.2及后续版本，在之前的版本中，只能使用普通算法

s = raw_input("请输入句子：")

screen_width = 80
text_width = len(s)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2

print
print ' ' * left_margin + '+' + '-' * (box_width-2) +	'+'
print ' ' * left_margin + '| ' + ' ' * text_width   +	' |'
print ' ' * left_margin + '| ' +        s           +	' |'
print ' ' * left_margin + '| ' + ' ' * text_width   +	' |'
print ' ' * left_margin + '+' + '-' * (box_width-2) + 	'+'
print
