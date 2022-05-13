# Chat_2.py

lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip()) #把line加入lines清单

for line in lines:
	s = line.split(' ')

	# 提取时间
	time = s[0][:5]
	# s清单的前5个characters(固定的时间部分，容易处理)
	# 可以将字串单独看作一个字串，这就是为什么可以使用[:5]
	print('Time is:', time)
	# 提取人名
	name = s[0][5:]
	print('Name is:', name)


		
