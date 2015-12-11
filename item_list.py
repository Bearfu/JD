__author__ = 'bear_fu'
# coding=utf-8
from bs4 import BeautifulSoup
import Deduplication
# 从主页的html文件中取出分类目录的地址，并写入到ＴＸＴ文件中


# 从本地读取爬到的静态网页，创建BeautifulSoup对象
def _JDURL():
	soup = BeautifulSoup(open("/Users/fuzhe/PycharmProjects/Python_other_Tools/Python_other_Tools/JD/jdhk.html", encoding="utf-8"))
	# 分类目录相关信息
	lists = soup.find_all('div', {'class': 'item'})
	# print(lists)
	for item in lists:
		href = item.find_all()
		for a in href:
			url = a.a
			if url is not None:
				try:
					name = a.a.string
					url = a.a['href']
					print(name)
					print(url)
					file.write(name + "@@@" + url + '\n')
				except:
					pass


if __name__ == '__main__':
	with open('JD_menu_urls.txt', mode='w', encoding="utf-8") as file:
		_JDURL()
	Deduplication._Deduplication("JD_menu_urls.txt", "JD_menu_url.txt")
	print("运行终了")


