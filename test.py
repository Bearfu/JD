# -*- coding:utf8 -*-
__author__ = 'bear_fu'
# encoding=utf-8
# maxpage = "1100"
# maxpage = int(maxpage)
# for page in range(maxpage):
# print(page)
import commodity_list

#
# import Deduplication
#
# Deduplication._Deduplication("00.log", "01.log")



# Python 去除HTML标签
# import mysql.connector
# import re
# import os
# import os.path
# root_dir = "F:\drug_detail"
# a = 0
# cnx = mysql.connector.connect(user='root', password='', database='ypt', charset="utf8")
# cursor = cnx.cursor()
# for parent, dirnames, filenames in os.walk(root_dir):
# for filename in filenames:
# 		name = filename.split("_")
# 		ID = name[0]
# 		#print(ID)
# 		host = root_dir+"/"+filename
# 		html = open(host, encoding="utf-8").read()
# 		dr = re.compile(r'<[^>]+>', re.S)
# 		text = dr.sub('', html)
# 		# 连接到数据库，并写入数据
# 		add_druginfo = ("INSERT INTO detail "
# 		               "(yptID, detail) "
# 						 "VALUES (%s,%s)")
# 		data_druginfo = (ID, text)
# 		cursor.execute(add_druginfo, data_druginfo)
# 		cnx.commit()
# 		a = a + 1
# 		print(str(a)+"/155683")
# 		#print(text)
#
# cursor.close()
# cnx.close()

# 进度条小工具
def _Progress_Bar(Task_Num, Max_num):
	presecte = round(Task_Num / Max_num, 4)
	presecte = int(presecte * 100)
	bar = presecte * 4
	print("运行进度" + str(presecte) + "%")


# 图片下载
def _Download_Picture():
	# -*- coding:utf-8 -*-
	import urllib.request

	path = "D:/Download"
	url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"
	name = "D:/download/1.jpg"
	# 保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片
	conn = urllib.request.urlopen(url)
	f = open(name, 'wb')
	f.write(conn.read())
	f.close()
	print('Pic Saved!')


if __name__ == '__main__':
	_Download_Picture()
