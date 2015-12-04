__author__ = 'bear_fu'
# 对TXT文件进行逐行去重


def _Deduplication(NameA, NameB):
	print("开始去重")
	obuff = []
	for ln in open(NameA, encoding="utf-8"):
		if ln in obuff:
			continue
		obuff.append(ln)
	with open(NameB, 'w', encoding="utf-8") as handle:
		handle.writelines(obuff)
		print("去重终了")


if __name__ == '__main__':
	print("去重开始")
	_Deduplication("JD_commodity_urls", "JD_commodity_url")
	print("去重终了")

