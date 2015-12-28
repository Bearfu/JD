__author__ = 'fuzhe'
import Creep_Tools
from selenium import webdriver

def Main(Star_Num,End_Num,mode):
	print(Star_Num)
	import time
	diver = webdriver.Firefox()
	# url = "http://jandan.net/ooxx/page-" + str(Star_Num) + "#comments"
	# print(url)
	for Page in range(int(Star_Num),int(End_Num)+1):
		if mode == "ooxx":
			url = "http://jandan.net/ooxx/page-" + str(Page)
		else:
			url = "http://jandan.net/pic/page-" + str(Page)
		diver.get(url)
		html = diver.page_source
		soup = Creep_Tools.Creep_Tools._html_to_soup(html)
		print("正在抓取第"+str(Page)+"页的数据")
		_Parser_for_one_url(soup)
		try:
			diver.find_element_by_class_name("next-comment-page").click()
			print("下一页")
		except:
			print("没有下一页了")
			break

	diver.quit()


# Max_page
def _Max_Page(soup):
	Max_Page = soup.find('div',{"class":"cp-pagenavi"})
	Max_Page = Max_Page.a.string
	return Max_Page

def _Parser_for_one_url(soup):
	url_list = []

	if soup is not None:
		Lists = soup.find_all('a',{'class','view_img_link'})
		# print(Lists)
		for list in Lists:
			list = str(list)
			a = list.split('"')
			print(a[3])
			url = str(a[3])
			file.write(url + "\n")


if __name__ == '__main__':
	#Main(950,1000)
	with open('JD_pic_url.txt', mode='w', encoding="utf-8") as file:
		# 开始页数 结束页数，传ooxx下妹子图，否则下无聊图
		Main(1000,1550,"ooxx")