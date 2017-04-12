# stock crawler by yangshuai
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re
import getstockvalue


def getstockurl(number):
    url = "http://stockpage.10jqka.com.cn/" + urllib.parse.quote(number)
    return url


def gettitle(number):
    url = getstockurl(number)
    response = urllib.request.urlopen(url)
    html = response.read()
    bsobj = BeautifulSoup(html, "html.parser")
    title = bsobj.find("a", href=re.compile(
        "ttp://stockpage.10jqka.com.cn/.+/")).strong.get_text()
    return title
# def getvale(number):


def main():
    number = input("->请输入一个正确的股票代码：")
    print('=' * 84 + '\n' + "|股票名称：{:^72}".format(gettitle(number)))
    getstockvalue.getstockvalue(number)
if __name__ == "__main__":
    main()
