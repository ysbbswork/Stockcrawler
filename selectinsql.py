# selectinsql.py
import time
import pymysql


def selectinsql(datatime, stocknumber):
    data_time_a = "a" + str(datatime)
    data_time_b = "b" + str(datatime)
    data_time_zxb = "zxb" + str(datatime)
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
        # 取操作
        cur.execute("select * from %s where number=%s" %
                    (data_time_a, stocknumber))
        rows = cur.fetchall()
        if rows == ():
            try:
                cur.execute("select * from %s where number=%s" %
                            (data_time_b, stocknumber))
                rows = cur.fetchall()
                if rows == ():
                    cur.execute("select * from %s where number=%s" %
                                (data_time_zxb, stocknumber))
                    rows = cur.fetchall()
                    if rows == ():
                        rows1 = "数据库中未查找到此股票数据\n"
                    else:

                        rows1 = str(rows[0]) + "\n"
                else:
                    rows1 = str(rows[0]) + "\n"
            except pymysql.err.ProgrammingError:
                return("数据库中未查找到此股票数据\n")
        else:
            rows1 = str(rows[0]) + "\n"

    except pymysql.err.ProgrammingError:
        return("请检查数据日期格式，数据库中没有当日数据\n")
    finally:
        cur.close()
        conn.close()
    return(rows1)


def main():
    a = input("number：")

    print(selectinsql(20170511, a))
if __name__ == "__main__":
    main()
