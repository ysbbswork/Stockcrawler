# getallstock.py
import urllib.request
from bs4 import BeautifulSoup
import pymysql
import pandas as pd
import time


def store(databox, k, data_time):

    try:
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='yangshuai87',
            db='test',
            use_unicode=1,
            charset='utf8')
        cur = conn.cursor()
        cur.execute("USE test")
        sql = """CREATE TABLE IF NOT EXISTS %s (number VARCHAR(6),name char(6),value1 char(6),value2 char(6),value3 char(6),value4 char(10),value5 char(10),value6 char(6))""" % (
            data_time)
        cur.execute(sql)
        for i in range(0, len(databox), k):
            # 存操作
            sql = "SELECT * FROM (%s) WHERE number = %s" % (data_time,
                                                            databox[i])
            # print(sql)
            cur.execute(sql)
            # print(type(number))
            if cur.rowcount == 0:
                sql = "INSERT INTO %s (number,name,value1,value2,value3,value4,value5,value6) VALUES (\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" % (
                    data_time, databox[i], databox[i + 1], databox[i + 2], databox[i + 3], databox[i + 4], databox[i + 6], databox[i + 7], databox[i + 8])
                cur.execute(sql)
                cur.connection.commit()
            else:  # 遇到重复的更新数据
                sql = "update %s set value1=\"%s\", value2=\"%s\", value3=\"%s\", value4=\"%s\", value5=\"%s\", value6=\"%s\" where number = \"%s\"" % (
                    data_time, databox[i + 2], databox[i + 3], databox[i + 4], databox[i + 6], databox[i + 7], databox[i + 8], databox[i])
                # print(sql)
                cur.execute(sql)
                # print("已经更新啦")

    finally:
        cur.close()
        conn.close()


def getranka():  # A股市场http://quote.stockstar.com/stock/szb_3_1_1.html
    for page in range(1, 1000000):
        databox = []
        # url1 = 'http://quote.stockstar.com/stock/ranklist_a_3_1_200.html'
        url1 = 'http://quote.stockstar.com/stock/ranklist_a_3_1_' + \
            str(page) + '.html'
        html = urllib.request.urlopen(url1)
        html = html.read().decode('gbk')  # 出现编码问题，解决
        bsobj = BeautifulSoup(html, "html.parser")
        databiglist = bsobj.findAll("td", {"class": "align_center "})
        if databiglist == []:  # 自行判断是否到达最后一面
            print("A股结束啦")
            break
        else:
            for data in databiglist:
                datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
                databox.append(data.get_text())
                for d in datalist:
                    databox.append(d.get_text())
            datatime = time.strftime('%Y%m%d', time.localtime(time.time()))
            data_time = "a" + datatime
            store(databox, 13, "%s" % data_time)
            print(page)
    return("A股爬完啦")


def getrankb():  # B股市场
    for page in range(1, 1000000):
        databox = []
        url1 = 'http://quote.stockstar.com/stock/ranklist_b_3_1_' + \
            str(page) + '.html'
        html = urllib.request.urlopen(url1)
        html = html.read().decode('gbk')  # 出现编码问题，解决
        bsobj = BeautifulSoup(html, "html.parser")
        databiglist = bsobj.findAll("td", {"class": "align_center "})
        if databiglist == []:
            print("B股结束啦")
            break
        else:
            for data in databiglist:
                datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
                databox.append(data.get_text())
                for d in datalist:
                    databox.append(d.get_text())
            datatime = time.strftime('%Y%m%d', time.localtime(time.time()))
            data_time = "b" + datatime
            store(databox, 13, "%s" % data_time)
            print(page)
    return("B股爬完啦")


def getrankzxb():  # 中小板

    for page in range(1, 1000000):
        databox = []
        # url1 = 'http://quote.stockstar.com/stock/ranklist_a_3_1_200.html'
        url1 = 'http://quote.stockstar.com/stock/small_3_1_' + \
            str(page) + '.html'
        html = urllib.request.urlopen(url1)
        html = html.read().decode('gbk')  # 出现编码问题，解决
        bsobj = BeautifulSoup(html, "html.parser")
        databiglist = bsobj.findAll("td", {"class": "align_center "})
        if databiglist == []:
            print("中小盘爬完啦！")
            break
        elif databiglist == [] and page != 1:
            print("给出的网页不符合要求，无法解析")
            break
        else:
            for data in databiglist:
                datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
                databox.append(data.get_text())
                for d in datalist:
                    databox.append(d.get_text())
            datatime = time.strftime('%Y%m%d', time.localtime(time.time()))
            data_time = "zxb" + datatime
            store(databox, 12, "%s" % data_time)
            print(page)  # 打印爬虫进度
    return("中小盘股爬完啦")


def getall():
    getranka()
    getrankb()
    getrankzxb()
    return("全部都爬完了")


def getstarstockurlstock(url):
    try:
        str(url)
        for page in range(1, 100000):
            databox = []
            url1 = url[0:-6] + str(page) + '.html'
            # print(url1)
            html = urllib.request.urlopen(url1)
            html = html.read().decode('gbk')  # 出现编码问题，解决
            bsobj = BeautifulSoup(html, "html.parser")
            databiglist = bsobj.findAll("td", {"class": "align_center "})
            if databiglist == [] and page != 1:
                print("指定股票市场爬完啦！")
                break
            elif databiglist == [] and page == 1:
                print("给出的网页不符合要求，无法解析")
                break
            else:
                for data in databiglist:
                    datalist = data.next_siblings  # bsobj的兄弟标签，不包含自己
                    databox.append(data.get_text())
                    for d in datalist:
                        databox.append(d.get_text())
                datatime = time.strftime('%Y%m%d', time.localtime(time.time()))
                data_time = "other" + datatime
                store(databox, 12, "%s" % data_time)
                print(page)  # 打印爬虫进度
        return("指定股市场爬完啦")
    except:
        return("链接非法")


def main():
    # getranka()
    # getrankb()
    # getrankzxb()
    # select()
    # print(getall())
    getstarstockurlstock("")
if __name__ == "__main__":
    main()
