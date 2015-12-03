__author__ = 'bear_fu'
# 对TXT文件进行逐行去重


def _Deduplication(NameA, NameB):
	obuff = []
	for ln in open(NameA + '.txt', encoding="utf-8"):
		if ln in obuff:
			continue
		obuff.append(ln)
	with open(NameB + '.txt', 'w', encoding="utf-8") as handle:
		handle.writelines(obuff)
		print("去重终了")


if __name__ == '__main__':
	_Deduplication("JD_menu+_url", "JD_index_url")
	print("去重终了")

