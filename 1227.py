#arr = [2,1,452,234,14]
#for i in range(1,len(arr)):
#	key =arr[i]
#	j = i - 1
#	while j >= 0:
#		if arr[j] > key:
#			arr[j+1] = arr[j]
#			arr[j] = key
#		j -= 1
#print arr
#
#
#arr = [2,1,452,234,14]
#for i in range(1,len(arr)):
#	key =arr[i]
#	j = i - 1
#	while j >= 0:
#		if arr[j] > key:
#			arr[j+1] = arr[j]
#			arr[j] = key
#		j -= 1
#print arr
#
#per = [168, 180, 170, 169]
#tmp_str = ''
#for i in range(0,len(per)-1):
#	for k in range(0,len(per)-1-i):
#			if per[k] > per[k+1]:
#				tmp_str =per[k+1]
#				per[k+1] = per[k]
#				per[k] = tmp_str
#print per
#
#


#arr = [1, 3, 4, 5, 's', 'a', 4, 's']
#print arr.index(4, 3)
#num_list = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#tmp = num_list.index(4)
#print tmp 
#print num_list.index(4, tmp+1)
#for i in range(len(num_list)):
#	if num_list[i] == 4:
#		print i

#arr = [1,2,3,2,4,2]
#brr = []
#for i in range(0,len(arr)):
#	brr.append(arr.pop())
#print brr #

#arr = [1,2,3,2,4,2]
#brr = []
#brr = arr[::-1]
#print brr #

#arr = [1,2,3,2,4,2]
#brr = []#

#for i in range(-(len(arr)-1), 1):
#	brr.append(arr[-i])
#print brr#
#

#arr = [1,2,3,2,4,2]
#for i in range(0,len(arr)/2):
#	arr[i],arr[-i - 1] = arr[-i - 1],arr[i]
#print arr





#num_list = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#new_list = []#

#for i in num_list:
#	if i not in new_list:
#		new_list.append(i)
#print new_list#

#arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
#new_list = []
#new_list1 = []
#for i in arr1:
#	if i not in new_list:
#		new_list.append(i)
#for j in new_list:
#	if j in arr2:
#		new_list1.append(j)
#print new_list1 #
#

#arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]
#new_list = []
#for i in arr1:
#	if i in arr2 and i not in new_list:
#		new_list.append(i)
#print new_list 



#arr = [2,1,452,234,14]
#key = ''
#for i in range(1,len(arr)):
#	key = arr[i]
#	j = i - 1
#	while j >= 0:
#		if arr[j] > key:
#			arr[j+1] = arr[j]
#			arr[j] =key
#		j -= 1
#print arr#

#arr = [2,1,452,234,14]
#for i in range(len(arr)-1,0,-1):
#	if arr[i] < arr[i-1]:
#		arr[i], arr[i-1] = arr[i-1], arr[i]
#print arr

#encoding: utf-8
#user_dict = {'aa': 123, 'bb': 456, 'cc': 789}
#new_dict = {}#

#for _key in user_dict:
#	_value= user_dict.get(_key)
#	print "%s => %s" % (_key, _value)
#	new_dict[_key] = _value
#	print 'new dict is %s' % new_dict
#print '--------'
#print new_dict
#new_dict['dd'] = 654
#print  'change new_dict'
#print new_dict
#print user_dict
#print id(new_dict)
#print id(user_dict)


#read_me = '''
#first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
#'''
#tmp_dict = {}
#for i in read_me:
#	if i not in tmp_dict:
#		tmp_dict[i] = 1
#	else:
#		tmp_dict[i] += 1 
#print tmp_dict#

#tmp_dict = {}
#for i in read_me:
#	if tmp_dict.get(i) is None:
#		tmp_dict[i] = 0
#	tmp_dict[i] += 1 
#print tmp_dict
#

#tmp_dict = {}
#for i in read_me:
#	tmp_dict.setdefault(i, 0)
#	tmp_dict[i] += 1 
#print tmp_dict#
#
#

#mylist = list("hello world")
#tmp_dict = {}
#for i in mylist:
#	tmp_dict[i] = None
#print tmp_dict

#

#user_dict = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
#tmp_dict = {}
#for key, value in user_dict.items():
#	if value in tmp_dict:
#		if isinstance(tmp_dict[value], list):
#			tmp_dict[value].append(key)
#		else:
#			tmp_dict[value] = [tmp_dict[value], key]
#	else:
#		tmp_dict.setdefault(value, key)
#	print tmp_dict
#print tmp_dict


#tmp_str ='abcDeF'
#tmp_str =tmp_str[0].upper() + tmp_str[1:].lower()
#print tmp_str#
#

#r_str =''
#r_list = []
#for i in 'reboot':
#	r_str = i + r_str
#	r_list.insert(0,i)
#print ''.join(r_list)
#print r_str#
#

#in_str = "user1:119,user2:112,user3:113"#

#tmp_list = in_str.split(',')
#print tmp_list
#for i in range(0,len(tmp_list)):
#	tmp_list[i]=tuple(tmp_list[i].split(':'))
#	print tmp_list[i]
#print tmp_list





read_me = '''
first of all, i want make it clear that i can not claim understanding this holy book  in just a few weeks, and i would not dare comment on this sacred book, in addition, i don't think i can give you a full picture of the holy bible in just few words.i can not preach anything here. what i want to do here is to express my understanding by sharing two events described in this book. the fist story i want to share is abandoned tower of babel.according to the bibel,people use the same language to communicate with each other in ancient times.with the soaring vanity,they decided to build a heaven-reaching tower to show off their achievement, god knows, he change the human language into different kinds and make it difficult for people to communicate with each other,hence the failure of building tower of  babel.this story tells people,never do things in selfishness, but make a life out of enternal glory.the other story,before jesus christ was crucified,he said, father,forgive them, for they know not what they do. with great love, he shouldered all the sins of  people. what can we learn from this story?we live in this world thanks to the love of god, for this reanson, we should make our lives glorious to honor our god.finally,i want to sum up by saying that only if we put our lives in the eternal love of god,can we live a perfect life, and  what you appealed is what god expected!
'''
tmp_dict = {}
for i in read_me:
	if i in tmp_dict:
		tmp_dict[i] += 1
	else:
		tmp_dict[i] = 1
print tmp_dict




user_dict = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}
tmp_dict = {}
for key, value in user_dict.items():
  if value in tmp_dict:
    if isinstance(tmp_dict[value], list):
      tmp_dict[value].append(key)
    else:
      tmp_dict[value] = [tmp_dict[value], key]
      print tmp_dict[value]
  else:
    tmp_dict.setdefault(value, key)
print tmp_dict


in_str = 'user1:119,user2;112,user3:113'
tmp_list = in_str.split(',')
print tmp_list
for i in range(0,len(tmp_list)):
  tmp_list[i]=tmp_list[i].split(':')
  tmp_list[i]=tuple(tmp_list[i])
  print tmp_list[i]
print tmp_list
