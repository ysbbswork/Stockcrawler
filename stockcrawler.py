# stock crawler by yangshuai
import urllib.request
import urllib.parse
import re


def getstockurl(number):
    url = "http://stockpage.10jqka.com.cn/" + str(number)
    return url


def gettitle(number):
    url = getstockurl(number)
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode('UTF-8', 'ignore')
    b = re.search(
        r'<strong>.+</strong>', html)
    title = re.search(r'>.+<', b.group()).group()
    return title


def getit(number):
    # i = 1
    # while i == 1:
    #     # try:
    #     number = input("->请输入一个正确的股票代码：")
    if str(number).isdigit():
        stocktitle = gettitle(number)
        # getstockvalue.getstockvalue(number)
        # elif number == "exit()":
        #     i = 0
        #     break
    else:
        print("warn:you should input a number!")
        # except :
        # print("None data")
    return stocktitle
if __name__ == "__main__":
    print(getit(600818))
