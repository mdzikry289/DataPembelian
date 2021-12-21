import tkinter as tk
from tkinter import ttk, messagebox
import pymysql.cursors
from tkinter import *

def GetValue(event):
 e1.delete(0, END)
 e2.delete(0, END)
 e3.delete(0, END)
 e4.delete(0, END)
 row_id = listBox.selection()[0]
 select = listBox.set(row_id)
 e1.insert(0,select['kode_brg'])
 e2.insert(0,select['nama_barang'])
 e3.insert(0,select['harga'])
 e4.insert(0,select['jumlah'])

def Add():
 kode_brg = e1.get()
 nama_barang = e2.get()
 harga = e3.get()
 jumlah = e4.get()

 mysqldb=pymysql.connect(host="localhost",user="root",password="",database="test")
 mycursor=mysqldb.cursor()
 
 try:
    sql = "INSERT INTO pembelian (kode_brg,nama_barang,harga,jumlah) VALUES (%s, %s, %s, %s)"
    val = (kode_brg,nama_barang,harga,jumlah)
    mycursor.execute(sql, val)
    mysqldb.commit()
    lastid = mycursor.lastrowid
    messagebox.showinfo("information", "Data pembelian berhasil disimpan!")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.focus_set()
 except Exception as e:
    print(e)
    mysqldb.rollback()
    mysqldb.close()

def update():
 kode_brg = e1.get()
 nama_barang = e2.get()
 harga = e3.get()
 jumlah = e4.get()
 mysqldb=pymysql.connect(host="localhost",user="root",password="",database="test")
 mycursor=mysqldb.cursor()
 try:
    sql = "Update pembelian set nama_barang= %s,harga= %s,jumlah= %s where kode_brg= %s"
    val = (nama_barang,harga,jumlah,kode_brg)
    mycursor.execute(sql, val)
    mysqldb.commit()
    lastid = mycursor.lastrowid
    messagebox.showinfo("information", "Record Updateddddd successfully...")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e1.focus_set()
 except Exception as e:
    print(e)
    mysqldb.rollback()
    mysqldb.close()

def delete():
 kode_brg = e1.get()

 mysqldb=pymysql.connect(host="localhost",user="root",password="",database="test")
 mycursor=mysqldb.cursor()

 try:
   sql = "DELETE FROM pembelian WHERE kode_brg = '%s'"
   val = (kode_brg)
   mycursor.execute(sql, val)
   mysqldb.commit()
   lastid = mycursor.lastrowid
   messagebox.showinfo("information", "Record Deleteeeee successfully...")
   e1.delete(0, END)
   e2.delete(0, END)
   e3.delete(0, END)
   e4.delete(0, END)
   e1.focus_set()
 except Exception as e:
   print(e)
   mysqldb.rollback()
   mysqldb.close()

def show():
 mysqldb = pymysql.connect(host="localhost", user="root", password="", database="test")
 mycursor = mysqldb.cursor()
 mycursor.execute("SELECT kode_brg,nama_barang,harga,jumlah FROM pembelian")
 records = mycursor.fetchall()
 print(records)
 for i, (kode_brg,nama_barang, harga,jumlah) in enumerate(records, start=1):
     listBox.insert("", "end", values=(kode_brg,nama_barang, harga, jumlah))
 mysqldb.close()

root = Tk()
root2 = Tk()
root.geometry("800x500")
root2.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Data Pembelian", fg="blue", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="Kode Barang").place(x=10, y=10)
Label(root, text="Nama Barang").place(x=10, y=40)
Label(root, text="Harga Barang").place(x=10, y=70)
Label(root, text="Jumlah Barang").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)

cols = ('kode_brg', 'nama_barang', 'harga','jumlah')
listBox = ttk.Treeview(root, columns=cols, show='headings' )

for col in cols:
 listBox.heading(col, text=col)
 listBox.grid(row=1, column=0, columnspan=2)
 listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()
root2.mainloop()