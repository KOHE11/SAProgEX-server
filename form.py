#! /usr/bin/env python3

import cgi
import sys
import io
import csv
import os
import psycopg2


def select_book(query):
    result = []
    print("query: ", query)

    # 空文字の時
    if query == "" or query == None:
        return result

    # 入力された文字を取得
    param_str_search = "%" + query + "%"

    # 該当する書籍を検索
    DATABASE_URL = os.environ.get('DATABASE_URL')
    con = psycopg2.connect(DATABASE_URL)
    cur = con.cursor()


    cur.execute('select * from booklist where TITLE ilike %s or AUTHOR ilike %s;', (param_str_search, param_str_search))
    rows = cur.fetchall()

    if not rows: # 検索結果が該当なしの時
        return result
    else:
        for i in range(len(rows)):
            dic = {}
            dic['ID'] = rows[i][0]
            dic['TITLE'] = rows[i][1]
            dic['AUTHOR'] = rows[i][2]
            dic['PUBLISHER'] = rows[i][3]
            dic['PRICE'] = rows[i][4]
            dic['ISBN'] = rows[i][5].replace(' ', '')
            result.append(dic)  
    cur.close()
    con.close()
    return result

if __name__=='__main__':
    print(select_book("java"))
