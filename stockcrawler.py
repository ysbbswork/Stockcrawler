# stock crawler by yangshuai
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


def getstockurl(number):
    url = "http://stockpage.10jqka.com.cn/" + urllib.parse.quote(number)
    return url


def main():
    url = getstockurl(input("->请输入一个正确的股票代码："))
    response = urllib.request.urlopen(url)
    html = response.read()
    bsobj = BeautifulSoup(html, "html.parser")
    title = bsobj.find("a", href=re.compile(
        "ttp://stockpage.10jqka.com.cn/.+/")).strong

    print(title.get_text())


if __name__ == "__main__":
    main()
