# getstockvalue.py单个股票获得data和gif
import urllib.request
import urllib.parse
import re
import os


def stocknumber(number):
    number1 = str(number)
    if number1.startswith("6"):
        stocknumber = "sh" + number1
    elif number1.startswith("0"):
        stocknumber = "sz" + number1
    else:
        stocknumber = number1
    return stocknumber


def getstockurl(number):
    number = stocknumber(number)
    url = "http://hq.sinajs.cn/list=" + number
    return url


def getstockgifurl(number):
    number = stocknumber(number)
    url = "http://image.sinajs.cn/newchart/daily/n/" + number + ".gif"
    return url


def format_info(data):
    # res = 'code: {data[1]} company: {data[2]} ' \
    #       'is checked: {dar}\n'.format(**data)
    # print(data)
    res = '=' * 7 + '\n'
    res += '|股票名称：{0[0]:<6}\n|今日开盘价：{0[1]:<6}\n|昨日收盘价：{0[2]:<6}\n|当前价格：{0[3]:<6}\n|今日最高价：{0[4]:<6}\n|今日最低价：{0[5]:<6}\n'.format(
        data)
    # res += '=' * 79 + '\n'
    res += '|一笔竞买价：{0[6]:<6}\n|一笔竞卖价：{0[7]:<6}\n|成交股票数：{0[8]:<12}\n|成交金额：{0[9]:<12}\n'.format(
        data)
    res += '=' * 7 + '\n'
    return res


def getstockvalue(number):
    valuenamelist = []

    url = getstockurl(number)
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode('gbk', 'ignore')
    a = re.search('".+"', html)
    b = a.group()
    # print(b)
    b = b[1:-1]
    # print(b)
    valuelist = b.split(",")
    # print(format_info(valuelist))
    # for value in valuelist:
    #     print(value)
    return format_info(valuelist)


def getgif(number):
    if os.path.exists("{0}.gif".format(number)) == True:
        # print("youla")
        pass
    else:
        url = getstockgifurl(number)
        response = urllib.request.urlopen(url)
        stock_gif = response.read()
        with open("{0}.gif".format(number), "wb") as f:
            f.write(stock_gif)


def main():
    number = input("->请输入一个正确的股票代码：")
    print(getstockvalue(number))
    # getgif(number)
if __name__ == "__main__":
    main()
