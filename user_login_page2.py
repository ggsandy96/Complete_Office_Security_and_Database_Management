from Tkinter import *
import MySQLdb
import os
def show_entry_fields():
	print "hello"
def ex():
	os.system('python /home/linaro/project/user_login.py &')
	close(master)

def chan():
	print "entered loop"
	global user
	db = MySQLdb.connect("localhost","root","root","testdb" )
	cursor = db.cursor()
	cursor.execute ("select username,password from login")
	data= cursor.fetchall()
	cursor.close ()
	print data
	a = len(data)
	for i in range(0,a):
		if(user == data[i][0]):
			pas=data[i][1]
	usr = e1.get()
	pwd = e2.get()
	pwd2= e3.get()
	e1.delete(0,END)
	e2.delete(0,END)
	e3.delete(0,END)
	Label(master, text="                      ").grid(row=8,column=3)
	if(pwd == pwd2):
		if(usr==pas):
			db = MySQLdb.connect("localhost","root","root","testdb" )
			cursor = db.cursor()
			cmd="delete from login where username='"+user+"'"
			cursor.execute (cmd)
			db.commit()
			cmd="INSERT INTO login (username,password) values('"+user+"','"+pwd+"')"
			cursor.execute (cmd)
			db.commit()
			cursor.close ()
			Label(master, text="changed successfully  ",fg="green").grid(row=9,column=3)
		else:
			Label(master, text="incorrect old password",fg="red").grid(row=9,column=3)
	else:
		Label(master, text="passwords not same    ",fg="red").grid(row=9,column=3)

def close(root):
	root.destroy()

def quit():
#	os.system('python home.py &')
	close(master)

master = Tk()

master.attributes("-fullscreen", True)
Label(master, text="                         ").grid(column=1, row=1)
Label(master, text="                         ").grid(column=2, row=1)
Label(master, text="                         ").grid(column=3, row=1)
Label(master, text="                         ").grid(column=4, row=1)
Label(master, text="                         ").grid(column=5, row=1)
Label(master, text="                         ").grid(column=6, row=1)
Label(master, text="                         ").grid(column=1, row=2)
Label(master, text="                         ").grid(column=2, row=2)
Label(master, text="                         ").grid(column=3, row=2)
Label(master, text="                         ").grid(column=4, row=2)
Label(master, text="                         ").grid(column=5, row=2)
Label(master, text="                         ").grid(column=6, row=2)
import MySQLdb
db = MySQLdb.connect("localhost","root","root","testdb" )
cursor = db.cursor()
cursor.execute ("select username from log")
log = cursor.fetchall()
cursor.close ()
user=log[-1]
print user
user=user[0]
user=str(user)
wel = "hello "+user
del log
Label(master, text=wel).grid(row=3,column=1)
Label(master, text="old password").grid(row=5,column=3)
Label(master, text="new password").grid(row=6,column=3)
Label(master, text="repeat new password").grid(row=7,column=3)
e1 = Entry(master,show="*")
e2 = Entry(master,show="*")
e3 = Entry(master,show="*")
e1.grid(row=5, column=4)
e2.grid(row=6, column=4)
e3.grid(row=7, column=4)
Button(master, text='change password', command=chan).grid(row=8, column=4)
Button(master, text='logout', command=ex).grid(row=3, column=6)

mainloop( )