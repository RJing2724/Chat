# Chat_1.py
# 大部分内容和Chat.py一样，但需要修改conversion部分
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
	person = None # 设定一个'无'的预设值

	# 设置计数
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_pic_count = 0
	viki_pic_count = 0

	for line in content: # 按顺序每行读取
# 进行对话统计，用split对字串里的空格进行切割
		s = line.split(' ') # split完之后变成list
# 变成list之后会发现所有对话中第0个位置都是时间，第一个位置都是人名，第二个位置及后续都是对话内容
		time = s[0]
		name = s[1]
# 将对话用人名区分开
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_pic_count += 1
			else:
				for message in s[2:]:
					allen_word_count += len(message)
			# 符号+=就是把len(m)加入allen_word_count
		
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pic_count += 1
			else:
				for message in s[2:]:
					viki_word_count += len(message)
	print('The word count of Allen is:', allen_word_count)
	print('The word count of Viki is:', viki_word_count)		
	print('The sticker count of Allen is:', allen_sticker_count)
	print('The sticker count of Viki is:', viki_sticker_count)
	print('The pic count of Allen is:', allen_pic_count)
	print('The pic count of Viki is:', viki_pic_count)
	

def write_file(filename, content): #不光要设计filename，不能忘记content
	with open(filename, 'w', encoding = 'utf-8-sig') as f:
		for line in content:
			f.write(line + '\n')



def main():
	content = read_file('LINE-Viki.txt')
	print(content)
	content = format_conversion(content)
	#output_file()
#	write_file('output_Line.txt', content)

main()








