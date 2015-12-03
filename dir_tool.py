__author__ = 'bear_fu'
# 在指定的路径创建文件夹

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


if __name__ == '__main__':
	# 定义要创建的目录
	mk_path = "F:\PycharmProjects\JD\dest"
	# 调用函数
	_mkdir(mk_path)