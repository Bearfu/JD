__author__ = 'bear_fu'
import Read_Line_by_Line
import commodity_list
# 从目录页获取更多的目录页信息
def _All_Index():
	# 读取部分目录信息，获取目录URL
	host_Url = Read_Line_by_Line._Read_Line_by_Line("JD_menu_url.txt")
	# print(host_Url)
	for host in host_Url:
		line = host.split('@@@')
		#print(line)
		index_url = line[1]
		# 解析URL得到soup
		soup = commodity_list._Analyze_Soup(index_url)
		# 测试用Url
		# url = "http://list.jd.hk/list.html?cat=1319%2C1525%2C1548&gjz=0&go=0"
		# soup = commodity_list._Analyze_Soup(url)
		# 爬取完整的目录URL信息
		try:
			lists = soup.find_all('ul', {'class': 'menu-drop-list clearfix'})
			for list in lists:
				index = list.find_all('li')
				for li in index:
					name = li.a.string
					url = li.a['href']
					print(name)
					head = "http://list.jd.hk"
					url = name + "@@@" + head + url
					print(url)
					# 写入txt文件
					file.write(url + "\n")
		except:
			pass
	print("运行终了")


if __name__ == '__main__':
	with open('JD_menu+_url.txt', mode='w', encoding="utf-8") as file:
		_All_Index()
	# 文件去重
	import Deduplication

	Deduplication._Deduplication("JD_menu+_url.txt", "JD_index_url.log")