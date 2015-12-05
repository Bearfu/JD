__author__ = 'bear_fu'
# 对TXT文件进行逐行去重


def _Deduplication(NameA, NameB):
	start_num = 0
	max_num = 995998
	print("开始对文件" + NameA + "去重")
	obuff = []
	for ln in open(NameA, encoding="utf-8"):
		if ln in obuff:
			start_num = start_num + 1
			continue
		obuff.append(ln)
		# 导入进度条---------------------------------------------------------------------------------------------------
		import test

		test._Progress_Bar(start_num, max_num)
	# ————————————————————————————————————————————————————————
	with open(NameB, 'w', encoding="utf-8") as handle:
		handle.writelines(obuff)
		print("去重终了")
		print("去重结果存放在" + NameB)


if __name__ == '__main__':
	_Deduplication("JD_commodity_urls.txt", "JD_commodity_urls.log")

