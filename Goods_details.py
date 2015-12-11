__author__ = 'bear_fu'
# 根据商品详情页的URL，获取商品信息并存入数据库
import re
import os
import json
import Creep_Tools
# 1.从log文中取出目录名称与



def _Main():
	All_Line_Arr = Creep_Tools.Read_Line_by_Line._Read_Line_by_Line("goods_id.log")
	for All_Line in All_Line_Arr:
		Line_arr = All_Line.split('@@@')
		commodity_index = Line_arr[0]
		commodity_url = Line_arr[1]
		ID_arr = commodity_url.split('.')
		ID = ID_arr[2]
		ID_arr = ID.split('/')
		ID = ID_arr[1]
		# 2.创建对应的文件夹
		code_picture_path = "E:/JD/" + commodity_index + "/" + ID + "/code_picture"
		detail_picture_path = "E:/JD/" + commodity_index + "/" + ID + "/detail_picture"
		Creep_Tools._mkdir(code_picture_path)
		# 3.获取网页的HTML文件
		import commodity_list
		# 4.解析网页的soup文件

		# 获取商品图片的
		soup = Creep_Tools._Analyze_Soup(commodity_url)
		ul = soup.find('ul', {'class': "lh"})
		if ul:
			all_li = ul.find_all('li')
			num = 0
			for li in all_li:
				num = num +1
				img = dict(li.contents[0].attrs)['data-url']
				img_url = 'https://img11.360buyimg.com/popWaterMark/%s' % (img)
				save_path = code_picture_path
				ID = ID + str(num)
				Creep_Tools._Download_Picture(img_url, ID, save_path)
		# 获取商品详情
		product_detail = get_product_detail(soup)
		print(product_detail)

		# 获取商品价格
		price = get_product_price(soup)
		print(price)
		savePath = get_datail_picture(soup)
		print(savePath)

		# 5.存储相应的文件


# 获取商品详情
def get_product_detail(soup):
	detail = list()
	import json

	div = soup.find('ul', {'id': 'parameter2'})
	all_li = div.find_all('li')
	for li in all_li:
		detail_content = li.string
		if detail_content is None:
			detail_content = '店铺：%s' % (li.get('title'))
		detail.append(detail_content)
	detail_json = json.dumps(detail, ensure_ascii=False)
	return detail_json


# 通过获取html，解析商品的名称
def get_product_name(self):
	div = self.html.find('div', {'class': "product-detail w"})
	# 取出商品的名称
	name = div.find('div', {'id': "name"}).h1.text  # 去除左端空格
	name = name.lstrip()
	return name

# 通过获取html，解析商品的价格
def get_product_price(soup):
	skuid = get_product_skuid(soup)
	url_skuid = 'http://p.3.cn/prices/get?skuid=J_%s&type=1' % (skuid)
	req = requests.get(url_skuid)
	content = BeautifulSoup(req.text)
	price_re = re.compile(r'"p":"(.*?)"', re.S)
	price = re.findall(price_re, str(content))[0]
	return price

# 通过获取的商品信息，获取商品的skuid
def get_product_skuid(soup):
	product_info = get_product(soup)
	skuid_re = re.compile(r'skuid:(.*?),')
	skuid = re.findall(skuid_re, product_info)[0]
	skuid = skuid.lstrip()
	return skuid


# 获取html中，商品的描述
def get_product(self):
	product_re = re.compile(r'product:(.*?);', re.S)
	product_info = re.findall(product_re, str(self.html))[0]
	return product_info

# 商品详情的图片
def get_datail_picture(soup):
		# 根据商品的product信息得到desc_url
	product_info = get_product(soup)
	skuid_re = re.compile(r'desc: \'(.*?)\',')
	desc_url = re.findall(skuid_re, product_info)[0]
	json_picture = 'http:%s?callback=showdesc' % (desc_url)
	req = requests.get(json_picture)
	content = BeautifulSoup(req.text, )
	picture_re = re.compile(r'data-lazyload=\'\\"(.*?)\\', re.S)
	picture_url = re.findall(picture_re, str(content))
	return picture_url


if __name__ == '__main__':
	_Main()