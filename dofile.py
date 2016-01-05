
try:
	raise BaseException('dadasd')
	0 + '33'
	print 4/0
except ZeroDivisionError as e:
     print e
except TypeError as e:
     print e
except BaseException as e:
     print e
print 'over'

h = opne('h.txt', 'w')
try:
	#raise BaseException('dadasd')
	pass
finally:
	print 'finally'
	h.close()
print 'over'

1.取出一条
2.提取出字符串
3.写入文件


{'[url,404]': '[ip,count]'}
{'url 404 ip': count}
