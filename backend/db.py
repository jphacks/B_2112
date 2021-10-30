from os import name
import MySQLdb
import mysql.connector
# import RakutenAPI
import time
import json
# from sql import sql_arg
from flask import Flask
# SQLARG=sql_arg()
from flask import jsonify
import requests

RAKUTEN_BOOKS_API_URL = "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404"
RAKUTEN_APP_ID = "1035792535946362350"
DATA_CONST={1:"id", 2:"title", 3:"author", 4:"publisher", 5:"buydate"}
TABLE_ORDER={1:"asc", 2:"desc"}


# データベースの作成(新規ユーザ登録)
def Initiate_DB(mailaddress):
    # MySQLへの接続の情報
    cnx = mysql.connector.connect(
        user='root',
        password='**',
        host='localhost',
        port='3306'
    )
    #接続
    cursor=cnx.cursor()
    #新規データベース作成
    cursor.execute("CREATE DATABASE "+mailaddress)
    # cursor.execute("SHOW DATABASES")
    # print(cursor.fetchall())
    cursor.close()
    
    #MySQLのデータベースへの接続情報
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='**',
        db=mailaddress,
        charset='utf8'
    )
    #接続
    cursor = connection.cursor()
    # テーブルの作成
    cursor.execute("""CREATE TABLE book_list(
    id INT(11) AUTO_INCREMENT NOT NULL, 
    title VARCHAR(100) NOT NULL COLLATE utf8mb4_unicode_ci, 
    author VARCHAR(100) NOT NULL COLLATE utf8mb4_unicode_ci, 
    publisher VARCHAR(20) NOT NULL COLLATE utf8mb4_unicode_ci, 
    imageurl VARCHAR(100) NOT NULL COLLATE utf8mb4_unicode_ci, 
    buydate VARCHAR(10) NOT NULL COLLATE utf8mb4_unicode_ci,
    PRIMARY KEY (id)
    )""")
    # 保存を実行
    connection.commit()

    # 接続を閉じる
    connection.close()

# 2:新規書籍登録関数
def Edit_DB(mailaddress,isbn,buydate):
    #MySQLのデータベースへの接続情報
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='**',
        db=mailaddress,
        charset='utf8'
    )
    #接続
    cursor = connection.cursor()
    #getDataにて情報取得とINSERT文作成
    insert_text=getData(isbn,buydate)
    #INSERT実行
    cursor.execute(insert_text)

    # 保存を実行
    connection.commit()

    # cursor.execute("SELECT * FROM book_list")
    # print(cursor.fetchall())

    # 接続を閉じる
    connection.close()

    return getallbooks(mailaddress)

# 本の情報をとってきて必要な要素だけ絞り出す
def getData(isbn,date):
    #情報をすべてAPIからとってくる
    data=get_book_info_by_isbn(isbn)
    # 利用規約的に一秒間で一アクセス以上するとだめらしい(今回は基本的に一個ずつしかアクセスしないから問題なし) 
    time.sleep(1)
    #使うデータだけ抽出
    title=data["title"]
    author=data["author"]
    publishername=data["publisherName"]
    imageurl=data["smallImageUrl"]
    #INSERT文作成
    text="INSERT INTO book_list (title, author,publisher,imageurl,buydate) VALUES(\'"+title+"\',\'"+author+"\',\'"+publishername+"\',\'"+imageurl+"\',\'"+date+"\')"
    return text

# 楽天のAPIに接続
def get_book_info_by_isbn(isbn):
    # requestのgetメソッドを利用してAPIにアクセス
    # &を介していろいろ検索条件追加できる
    #今回はisbnで情報を一つに確定
    response = requests.get("{}?format=json&isbnjan={}&applicationId={}".format(RAKUTEN_BOOKS_API_URL,isbn, RAKUTEN_APP_ID))
    return response.json()["Items"][0]["Item"]



# 3:Data削除
def delete_DB(mailaddress,pri_id):
    #MySQLのデータベースへの接続情報
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='**',
        db=mailaddress,
        charset='utf8'
    )
    cursor = connection.cursor()

    sql = ("DELETE FROM book_list WHERE id = %s")

    param = (pri_id,)

    cursor.execute(sql, param)

    # 保存を実行
    connection.commit()

    cursor.execute("SELECT * FROM book_list")
    print(cursor.fetchall())

    # 接続を閉じる
    connection.close()


# 4:データをJson形式に変換して出力
def getallbooks(mailaddress):
    booklist_temp = get_all_book_data(mailaddress)
    print('本情報一覧表示')
    booklist = []
    for i in booklist_temp:
        # print(i)
        pri_id=i[0]
        title = i[1]
        author = i[2]
        publisher = i[3]
        imageurl=i[4]
        buydate=i[5]
        bookinfo = {
            'id':pri_id,
            'title': title,
            'author':author,
            'publisher':publisher,
            'imageurl':imageurl,
            'buydate':buydate
        }
        booklist.append(bookinfo)
        
    # return json.dumps(booklist,ensure_ascii=False)
    return jsonify(booklist)

#MySQLに接続してデータをとってくるand並び替えもココ
def get_all_book_data(mailaddress):
    #MySQLのデータベースへの接続情報
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        passwd='**',
        db=mailaddress,
        charset='utf8'
    )
    cursor = connection.cursor()

    sql = "select id,title,author,publisher,imageurl,buydate from book_list"
    cursor.execute(sql)
    book_data = cursor.fetchall()
    print(book_data)
    return book_data

#test code
if __name__ == '__main__':
    address=input("メールアドレスを入力")
    while True:
        i=int(input("1:DB作成 2:本登録 3:Data削除 4:json出力"))
        if i == 1:
            Initiate_DB(address)
        elif i == 2:
            isbn=input("isbnを入力")
            date=input("登録日を入力")
            Edit_DB(address,isbn,date)
        elif i == 3:
            id =input("idを入力")
            delete_DB(address,id)
        elif i==4:
            element=int(input("タイトル:1,著者:2,出版社:3,購入順:4,登録順:5"))
            order=int(input("昇順:1, 降順:2"))
            getallbooks(address)
        else :
            break