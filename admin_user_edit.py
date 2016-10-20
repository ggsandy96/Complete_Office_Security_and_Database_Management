from Tkinter import *
import MySQLdb
import os

def close(root):
	root.destroy()

def cha():
	db = MySQLdb.connect("localhost","root","root","testdb" )
	cursor = db.cursor()
	usr = e1.get()
	pwd = e2.get()
	e1.delete(0,END)
	e2.delete(0,END)
	cmd="update login set password='"+pwd+"' where username='"+usr+"'"
	cursor.execute (cmd)
	db.commit()
	cursor.close ()
	Label(master, text="changed successfully  ",fg="green").grid(row=8,column=3)

def add():
	db = MySQLdb.connect("localhost","root","root","testdb" )
	cursor = db.cursor()
	usr = e3.get()
	pwd = e4.get()
	e3.delete(0,END)
	e4.delete(0,END)
	cmd="INSERT INTO login (username,password) values('"+usr+"','"+pwd+"')"
	cursor.execute (cmd)
	db.commit()
	cursor.close ()
	Label(master, text="inserted successfully  ",fg="green").grid(row=13,column=3)


def quit():
#	os.system('python home.py &')
	close(master)

master = Tk()

master.attributes("-fullscreen", True)
Label(master, text="                              ").grid(column=1, row=1)
Label(master, text="                              ").grid(column=1, row=3)
Label(master, text="                              ").grid(column=1, row=4)
Label(master, text="                              ").grid(column=1, row=5)
Label(master, text="                              ").grid(column=1, row=6)
Label(master, text="                              ").grid(column=1, row=7)
Label(master, text="                              ").grid(column=1, row=8)
Label(master, text="                              ").grid(column=2, row=1)
Label(master, text="                              ").grid(column=3, row=1)
Label(master, text="                              ").grid(column=4, row=1)
Label(master, text="                              ").grid(column=5, row=1)
Label(master, text="                              ").grid(column=6, row=1)
Label(master, text="                              ").grid(column=1, row=2)
Label(master, text="                              ").grid(column=2, row=2)
Label(master, text="                              ").grid(column=3, row=2)
Label(master, text="                              ").grid(column=4, row=2)
Label(master, text="                              ").grid(column=5, row=2)
Label(master, text="                              ").grid(column=6, row=2)
Label(master, text="                              ").grid(column=7, row=2)
Label(master, text="                              ").grid(column=8, row=2)
Label(master, text="                              ").grid(column=9, row=2)


db = MySQLdb.connect("localhost","root","root","testdb" )
cursor = db.cursor()
cursor.execute ("select username from login")
lst = cursor.fetchall()
lst=zip(*lst)
cursor.close ()
label=Label(master,text="username").grid(column=4,row=5)
label=Label(master,text="password").grid(column=4,row=6)
label=Label(master,text="username").grid(column=4,row=9)
label=Label(master,text="password").grid(column=4,row=10)
label=Label(master,text="\n".join(map(str,lst[0]))).grid(column=5, row=20)

e1 = Entry(master)
e1.grid(row=5, column=5)
e2 = Entry(master,show="*")
e2.grid(row=6, column=5)
e3 = Entry(master)
e3.grid(row=9, column=5)
e4 = Entry(master,show="*")
e4.grid(row=10, column=5)

Button(master, text='change password', command=cha).grid(row=7, column=5)
Button(master, text='add new user', command=add).grid(row=11, column=5)
Button(master, text='exit', command=quit).grid(row=12, column=5)
mainloop( )
