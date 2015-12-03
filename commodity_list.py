__author__ = 'bear_fu'
from bs4 import BeautifulSoup
import Deduplication
import requests


# 从商品展示页的html文件中取出单个商品的地址，并写入到ＴＸＴ文件中
# 获取目录页面内的所有商品网址信息并写入到文件中
# 从TXT文件中获取url
def _catch_Index_Url():
	print("开始从TXT文件中获取url")
	resource_file = open("JD_index_url.txt", "r", encoding="utf-8")
	while True:
		in_line = resource_file.readline()
		if in_line:
			in_line = in_line.strip("\n")
			# 将目录名与目录url分离
			line = in_line.split('@@@')
			index_name = line[0]
			index_url = line[1]
			# 获取此URL下的soup
			soup = _Analyze_Soup(index_url)
			# 获取此URL下的最大页数
			Max_Pag = int(_Page_num(soup))
			try:
				for page in range(Max_Pag):
					print(page)
					if page >= 1:
						page = "&page=" + str(page)
						print(page)
						try:
							url = index_url + page
							soup = _Analyze_Soup(url)
							if soup is not None:
								# 获取此URL下的所有商品页面的URL
								url_list = parser_for_one_url(soup)
								for url in url_list:
									print(index_name + "," + url)
									commdity_url = index_name + "," + url
									file.write(commdity_url + '\n')
							else:
								pass
						except:
							pass
					else:
						pass
			except:
				pass
	resource_file.close()


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
			return "1"
	else:
		return "1"


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
	Deduplication._Deduplication("JD_commodity_urls", "JD_commodity_url")
	# print("运行开始")
	# soup =_Analyze_Soup("http://list.jd.hk/list.html?cat=1319,1525,7057&go=0&gjz=0")
	# parser_for_one_url(soup)
	print("运行终了")
