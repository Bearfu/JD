__author__ = 'fuzhe'


class Creep_Tools:

	# 在指定的路径创建文件夹
	# 若已经存在打印目录存在
	# 若不存在则依次创建文件夹，并返回创建成功
	# Input 创建文件夹的路径
	def _mkdir(path):
		# 引入模块
		import os

		# 去除首位空格
		path = path.strip()
		# 去除尾部 \ 符号
		path = path.rstrip("\\")

		# 判断路径是否存在
		# 存在     True
		# 不存在   False
		is_Exists = os.path.exists(path)

		# 判断结果
		if not is_Exists:
			# 如果不存在则创建目录
			print(path + ' 创建成功')
			# 创建目录操作函数
			os.makedirs(path)
			return True
		else:
			# 如果目录存在则不创建，并提示目录已存在
			print(path + ' 目录已存在')
			return False

	# 逐行读取文件并将其作为数组返回
	# Input 文件路径以及文件名称
	# Output 包含文件内容的数组，可能出现空
	def _Read_Line_by_Line(path):
		all_line = []
		for line in open(path, encoding="utf-8"):
			line = line.strip("\n")
			all_line.append(line)
		print(all_line)

		return all_line

	# 文件去重
	# Input 需要去重的文件路径以及名称
	# 运行完成后源文件按行去重
	def _Deduplication(Name):
		# 检查文件行数
		start_num = 1
		Max_num = Creep_Tools._Line_number(Name)
		print("开始对文件" + Name + "去重")
		obuff = []
		for ln in open(Name, encoding="utf-8"):
			if ln in obuff:
				start_num = start_num + 1
				continue
			obuff.append(ln)
		# 导入进度条
			Creep_Tools._Progress_Bar(start_num, Max_num)
		# 创建文件B
		with open(Name, 'w', encoding="utf-8") as handle:
			handle.writelines(obuff)
			print("去重终了")
			print("去重结果存放在" + Name)

	# 文件最大行数
	def _Line_number(Name):
		lines =len(open(Name, encoding="utf-8").readlines())
		return lines

	# 进度条小工具
	def _Progress_Bar(Task_Num, Max_num):
		presecte = round(Task_Num / Max_num, 4)
		presecte = int(presecte * 100)
		bar = presecte * 4
		print("运行进度" + str(presecte) + "%")

	# 获取路径的soup文件
	# input 需要解析的网址URL
	# output 解析出的soup文件
	# 若无法解析则返回None
	def _Analyze_Soup(url):
		import requests
		from bs4 import BeautifulSoup
		try:
			responce = requests.get(url, timeout=1)
		except:
			responce = None
		if responce is not None:
			soup = BeautifulSoup(responce.text, )
			return soup
		else:
			return None


	# 图片下载
	# Input 图片的下载路径，图片的存储名称，图片的存储路径
	def _Download_Picture(url, name, save_path):
		import  urllib
		image_name = save_path + "/" + name + ".jpg"
		# 保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
		conn = urllib.request.urlopen(url)
		f = open(image_name, 'wb')
		f.write(conn.read())
		f.close()
		print('Pic Saved!')

	# Beautsoup解析
	def _html_to_soup(html):
		from bs4 import BeautifulSoup
		with open('1.html',mode="w",encoding="utf-8")as file:
			file.write(html)
		soup = BeautifulSoup(open("1.html",encoding="utf-8"))
		return soup




if __name__ == '__main__':
	Creep_Tools._Deduplication("1.log")