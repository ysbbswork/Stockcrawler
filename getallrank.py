# getallrank.py
import urllib.request
from bs4 import BeautifulSoup


def format_info(databox, k):
    # 代码    简称  最新价 涨跌幅 涨跌额 5分钟涨幅   成交量(手) 成交额(万元)   换手率 振幅  量比  委比  市盈率
    res = '=' * 7 + '\n'
    for i in range(0, len(databox), k):
        res += '|代码：{0:<6}|简称：{1:<5}|最新价：{2:<6}|涨跌幅：{3:<6}|涨跌额：{4:<6}|成交额(万元)：{5:<6}|换手率：{6:<6}\n'.format(
            databox[i], databox[i + 1], databox[i + 2], databox[i + 3], databox[i + 4], databox[i + 6], databox[i + 8])
    res += '=' * 7 + '\n'
    return res


def getranka():  # A股市场
    url1 = 'http://quote.stockstar.com/stock/ranklist_a.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []

    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    # for i in range(0, len(databox), 13):
    res = format_info(databox, 13)
    return(res)


def getrankb():  # B股市场
    url1 = 'http://quote.stockstar.com/stock/ranklist_b.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    # for i in range(0, len(databox), 13):
    res = format_info(databox, 13)
    return(res)


def getrankha():  # 沪市A股
    url1 = 'http://quote.stockstar.com/stock/sha.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    res = format_info(databox, 12)
    return(res)


def getranksa():  # 深市A股
    url1 = 'http://quote.stockstar.com/stock/sza.shtml'
    html = urllib.request.urlopen(url1)
    bsobj = BeautifulSoup(html, "html.parser")
    html = html.read().decode('gbk')  # 出现编码问题，解决
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    res = format_info(databox, 12)
    return(res)


def getrankhb():  # 沪市B股
    url1 = 'http://quote.stockstar.com/stock/shb.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    res = format_info(databox, 12)
    return(res)


def getranksb():  # 深市B股
    url1 = 'http://quote.stockstar.com/stock/szb.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    res = format_info(databox, 12)
    return(res)


def getrankzxb():  # 中小板
    url1 = 'http://quote.stockstar.com/stock/small.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    res = format_info(databox, 12)
    return(res)


def getrankcyb():  # 创业板
    url1 = 'http://quote.stockstar.com/stock/gem.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())

    res = format_info(databox, 12)
    return(res)


def getranknew():  # 新股
    url1 = 'http://quote.stockstar.com/stock/ipo.shtml'
    html = urllib.request.urlopen(url1)
    html = html.read().decode('gbk')  # 出现编码问题，解决
    bsobj = BeautifulSoup(html, "html.parser")
    databiglist = bsobj.findAll("td", {"class": "align_center "})

    databox = []
    for data in databiglist:
        datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
        databox.append(data.get_text())
        for d in datalist:
            databox.append(d.get_text())
    print(len(databox))
    res = format_info(databox, 12)
    return(res)


def main():
    print(getranknew())
if __name__ == "__main__":
    main()
