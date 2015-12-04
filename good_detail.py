# coding=utf-8
__author__ = 'zhaoyun'

import re
import os
import json
import requests
import pymysql
from bs4 import BeautifulSoup

# from time import time
# t = time()

goods_id = open("goods_id.log", "r", encoding="utf-8")
err_url = open("err_url.log", "w", encoding="utf-8")

class Craw(object):
    # 初始化，请求，解析
    def __init__(self, url):
        self.url = url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        try:
            req = requests.get(self.url, headers=headers)
            self.html = BeautifulSoup(req.text, from_encoding='gb2312')
        except:
            print("网络错误:" + url)
            err_url.write(url)
            pass

    # 获取html中，商品的描述
    def get_product(self):
        product_re = re.compile(r'product:(.*?);', re.S)
        product_info = re.findall(product_re, str(self.html))[0]
        return product_info

    # 通过获取的商品信息，获取商品的skuid
    def get_product_skuid(self):
        product_info = self.get_product()
        skuid_re = re.compile(r'skuid:(.*?),')
        skuid = re.findall(skuid_re, product_info)[0]
        skuid = skuid.lstrip()
        return skuid

    # 通过获取html，解析商品的名称
    def get_product_name(self):
        div = self.html.find('div', {'class': "product-detail w"})
        # 取出商品的名称
        name = div.find('div', {'id': "name"}).h1.text
        # 去除左端空格
        name = name.lstrip()
        return name

    # 通过获取html，解析商品的价格
    def get_product_price(self):
        skuid = self.get_product_skuid()
        url_skuid = 'http://p.3.cn/prices/get?skuid=J_%s&type=1' % (skuid)
        req = requests.get(url_skuid)
        content = BeautifulSoup(req.text, from_encoding='gb2312')
        price_re = re.compile(r'"p":"(.*?)"', re.S)
        price = re.findall(price_re, str(content))[0]
        return price

    # """根据url获取文件名"""
    def gGetFileName(self, url):
        if url is None: return None
        if url is "": return ""
        arr = url.split("/")
        return arr[len(arr) - 1]

    # """根据url下载文件，文件名参数指定"""
    def gDownloadWithFilename(self, url, savePath, file):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                with open(savePath + '/' + file, 'wb') as f:
                    for chunk in r:
                        f.write(chunk)
        except IOError as error:
            print("DOWNLOAD %s ERROR!==>>%s" % (url, error))
        except Exception as e:
            print("Exception==>>" + e)

    # """根据url下载文件，文件名自动从url获取"""
    def gDownload(self, url, savePath):
        fileName = self.gGetFileName(url)
        self.gDownloadWithFilename(url, savePath, fileName)

    # 根据id建立下一层文件夹
    def down_img(self, img_url, function):
        skuid = self.get_product_skuid()
        savePath = 'product_picture/%s/%s' % (skuid,function)
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        self.gDownload(img_url, savePath)
        return savePath

    # 商品高清大图片
    def get_product_picture(self):
        ul = self.html.find('ul', {'class': "lh"})
        if ul:
            all_li = ul.find_all('li')
            for li in all_li:
                img = dict(li.contents[0].attrs)['data-url']
                img_url = 'https://img11.360buyimg.com/popWaterMark/%s' % (img)
                savePath = self.down_img(img_url,'product_img')
        return savePath

    # 商品详情正文
    def get_product_detail(self):
        detail = list()
        div = self.html.find('ul', {'id': 'parameter2'})
        all_li = div.find_all('li')
        for li in all_li:
            detail_content = li.string
            if detail_content is None:
                detail_content = '店铺：%s' % (li.get('title'))
            detail.append(detail_content)
        detail_json = json.dumps(detail, ensure_ascii=False)
        return detail_json

    # 商品详情的图片
    def get_datail_picture(self):
        # 根据商品的product信息得到desc_url
        product_info = self.get_product()
        skuid_re = re.compile(r'desc: \'(.*?)\',')
        desc_url = re.findall(skuid_re, product_info)[0]
        json_picture = 'http:%s?callback=showdesc' % (desc_url)
        req = requests.get(json_picture)
        content = BeautifulSoup(req.text, from_encoding='gb2312')
        picture_re = re.compile(r'data-lazyload=\'\\"(.*?)\\', re.S)
        picture_url = re.findall(picture_re, str(content))
        for img_url in picture_url:
            savePath = self.down_img(img_url, 'datail_img')
        return savePath

    def extract(self):
        skuid = self.get_product_skuid()
        price = self.get_product_price()
        name = self.get_product_name()
        savePath1 = self.get_product_picture()
        detail= self.get_product_detail()
        savePath2 = self.get_datail_picture()

        print("==========商品基本信息==============")
        # 输出内容
        print("商品ID：" + skuid)
        print("商品名称：" + name)
        print("商品价格：" + price)
        print("商品图片下载在：" + savePath1)
        print("商品详情：" + detail)
        print("详情图片下载在：" + savePath2)


if __name__ == '__main__':
    if not os.path.exists("product_picture"):
        os.mkdir("product_picture")
    while 1:
        in_line = goods_id.readline()
        if in_line:
            url = in_line.strip("\n")
            jp = Craw(url)
            jp.extract()
        else:
            break

# print ("total run time:")
# print (time()-t)