__author__ = 'bear_fu'
from bs4 import BeautifulSoup
import Deduplication
import requests
import Read_Line_by_Line
import test

# 从商品展示页的html文件中取出单个商品的地址，并写入到ＴＸＴ文件中
# 获取目录页面内的所有商品网址信息并写入到文件中

def _catch_Index_Url():
	a = 0
	Max_line = 247
	# 从TXT文件中获取url
	All_line = Read_Line_by_Line._Read_Line_by_Line("JD_index_url.log")
	for line in All_line:
		if line is not '':
			print(line)
			a = a + 1
			line_arr = line.split('@@@')
			index_name = line_arr[0]
			index_url = line_arr[1]
			# 测试用URL
			# index_url = "http://list.jd.hk/9855-9857-9914.html"
			# 获取此URL下的soup
			soup = _Analyze_Soup(index_url)
			# 获取此URL下的最大页数
			Max_Pag = int(_Page_num(soup))
			print(index_name + "MAX_Pag" + str(Max_Pag))
			if Max_Pag == 0:
				print(Max_Pag)
			elif Max_Pag == 1:
				try:
					print("Max_Pag = 1")
					url = index_url
					soup = _Analyze_Soup(url)
					if soup is not None:
						# 获取此URL下的所有商品页面的URL
						url_list = parser_for_one_url(soup)
						for url in url_list:
							test._Progress_Bar(a, Max_line)
							commdity_url = index_name + "@@@" + url
							print(commdity_url)
							file.write(commdity_url + '\n')
					else:
						pass
				except:
					pass
			else:
				try:
					for page in range(1, Max_Pag):
						page = "&page=" + str(page)
						print(index_name + page)
						try:
							url = index_url + page
							soup = _Analyze_Soup(url)
							if soup is not None:
								# 获取此URL下的所有商品页面的URL
								url_list = parser_for_one_url(soup)
								for url in url_list:
									test._Progress_Bar(a, Max_line)
									commdity_url = index_name + "@@@" + url
									print(commdity_url)
									file.write(commdity_url + '\n')
							else:
								pass
						except:
							pass
				except:
					pass
	print("")


# 获取路径的soup文件
# input 需要解析的网址URL
# output 解析出的soup文件
def _Analyze_Soup(url):
	try:
		responce = requests.get(url, timeout=1)
	except:
		responce = None
	if responce is not None:
		soup = BeautifulSoup(responce.text, )
		return soup
	else:
		return None


# 最大页数
# input 页面的soup文件
# output 当前页面的最大页数
def _Page_num(soup):
	if soup is not None:
		page = soup.find('span', {'class': 'fp-text'})
		try:
			maxpage = page.i.string
			return maxpage
		except:
			return "0"
	else:
		return "0"


# 获取单页内容
# input soup文件
# output 抓取到的网址路径
def parser_for_one_url(soup):
	url_list = []
	try:
		lists = soup.find_all('ul', {'class': 'gl-warp clearfix'})
		for item in lists:
			hrefs = item.find_all()
			for herf in hrefs:
				names = herf.find_all('div', {'class': 'p-name'})
				for name in names:
					url = name.a['href']
					if url is not None:
						try:
							url_list.append(url)
						except:
							pass
					else:
						print("soup为空")
	except:
		pass
	return url_list


if __name__ == '__main__':
	with open('JD_commodity_urls.txt', mode='w', encoding="utf-8") as file:
		_catch_Index_Url()
	Deduplication._Deduplication("JD_commodity_urls.txt", "JD_commodity_url.log")
	print("运行终了")
	print("运行结果存放在_JD_commodity_urls.txt")


