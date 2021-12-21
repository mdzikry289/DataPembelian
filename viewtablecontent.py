import tkinter as tk
from tkinter import ttk, messagebox
import pymysql.cursors
from tkinter import *

# db = pymysql.connect(‘localhost’,’root’,’ ’,’test’)
db = pymysql.connect(host='localhost',user='root',password='',database='test',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
cursor = db.cursor()

sql = """SELECT * FROM PEMBELIAN"""
cursor.execute(sql)
myresult = cursor.fetchall()
 
for x in myresult:
    print(x)