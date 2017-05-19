import pymysql
import pandas as pd
import time


def pandait(data_time, key1="", key2="", key3=""):
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
        cur.execute(
            "select number,name,value1,value2,value3,value4,value5,value6 from %s" % data_time)
        rows = cur.fetchall()
        # print(rows)#row 是一个好的结构！
        df = pd.DataFrame([ij for ij in i]for i in rows)

        # p_float = df[3].str.strip("%").astype(float) / 100
        p_float2 = df[2].str.strip("%").astype(float)
        df['p_float2'] = p_float2
        p_float5 = df[5].str.strip("%").astype(float)
        df['p_float5'] = p_float5
        p_float6 = df[6].str.strip("%").astype(float)
        df['p_float6'] = p_float6
        if key3 != "":
            key3 = int(key3)
            df = df.sort_values(
                by=['p_float6'], ascending=[key3])
        if key2 != "":
            key2 = int(key2)
            df = df.sort_values(
                by=['p_float5'], ascending=[key2])
        if key1 != "":
            key1 = int(key1)
            df = df.sort_values(
                by=['p_float2'], ascending=[key1])

        # print(df[[0, 1, 2, 3, 4, 5, 6, 7]].head(10))
        return(df[[0, 1, 2, 3, 4, 5, 6, 7]].head(30))
    except pymysql.err.ProgrammingError:
        return("请输入正确存在的数据库")
    finally:
        cur.close()
        conn.close()


def main():
    # a = int(input())
    # print(type(a))
    print(pandait("a20170508", 0, 0, 0))
    # b = int(input())
    # print(type(b))
    # print(pandait("a20170508", b, 2, 2))
if __name__ == "__main__":
    main()
