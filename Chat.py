# Chat.py

import os

# Give the system permission to search file



# Open and read the file, put the strings in the txt into a list.
def read_file(filename):
	content = [] # Set lists
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # sig用来去掉"\ufeff"
		for line in f:
			content.append(line.strip())
	return content


def format_conversion(content):
	new = []
	person = None # 设定一个'无'的预设值
	for line in content: # 按顺序每行读取
		if line == 'Allen':
			person = 'Allen'
			continue

		elif line == 'Tom':
			person = 'Tom'
			continue

		if person: # 当person有value时执行以下
			new.append(person + ':' + line)
		# 以人名 + ‘：’ + line的形式填入new

	return(new)

def write_file(filename, content): #不光要设计filename，不能忘记content
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in content:
			f.write(line + '\n')



def main():
	content = read_file('input.txt')
	print(content)
	content = format_conversion(content)
	#output_file()
	write_file('output.txt', content)

main()








