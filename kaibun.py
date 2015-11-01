import copy

def to2shin(num):
	array = []
	while num>0:
		array.append(num % 2)
		num = num//2
	array.reverse()
	return array

def to8shin(num):
	array = []
	while num>0:
		array.append(num % 8)
		num = num//8
	array.reverse()
	return array

for i in range(10,1000):
	flag = 1
	a = list(str(i))
	b = copy.deepcopy(a)
	a.reverse()
	if (a!=b):
		flag = 0

	a = to2shin(i)
	b = copy.deepcopy(a)
	a.reverse()
	if (a!=b):
		flag = 0

	a = to8shin(i)
	b = copy.deepcopy(a)
	a.reverse()
	if (a!=b):
		flag = 0

	if flag == 1:
		print(i)