# __author__ = 'bear_fu'
# maxpage = "1100"
# maxpage = int(maxpage)
# for page in range(maxpage):
# print(page)
import commodity_list

url = "http://search.jd.hk/Search?keyword=morning%20fresh&enc=utf-8"
soup = commodity_list._Analyze_Soup(url)
commodity_url = commodity_list.parser_for_one_url(soup)
print(commodity_url)