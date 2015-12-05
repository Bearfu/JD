__author__ = 'bear_fu'


def _Read_Line_by_Line(host):
	all_line = []
	for line in open(host, encoding="utf-8"):
		line = line.strip("\n")
		all_line.append(line)
	print(all_line)

	return all_line


if __name__ == '__main__':
	host = "JD_index_url.txt"
	_Read_Line_by_Line(host)