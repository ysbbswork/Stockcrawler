# getstockvalue.py
import urllib.request
import urllib.parse
import re


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
    url = "http://hq.sinajs.cn/list=" + stocknumber(number)
    return url


def format_info(data):
    # res = 'code: {data[1]} company: {data[2]} ' \
    #       'is checked: {dar}\n'.format(**data)

    res = '=' * 84 + '\n'
    res += '|今日开盘价：{0[1]:<6}|昨日收盘价：{0[2]:<6}|当前价格：{0[3]:<6}|今日最高价：{0[4]:<6}|今日最低价：{0[5]:<6}|\n'.format(
        data)
    res += '=' * 84 + '\n'
    res += '|一笔竞买价：{0[6]:<6}|一笔竞卖价：{0[7]:<6}|成交股票数：{0[8]:<12}|成交金额：{0[9]:<12}\n'.format(
        data)
    return res


def getstockvalue(number):
    valuenamelist = []

    url = getstockurl(number)
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode('UTF-8', 'ignore')
    a = re.search(r'".+"', html)
    b = a.group()
    valuelist = b.split(",")
    print(format_info(valuelist))
    # for value in valuelist:
    #     print(value)


def main():
    number = input("->请输入一个正确的股票代码：")
    getstockvalue(number)
if __name__ == "__main__":
    main()
