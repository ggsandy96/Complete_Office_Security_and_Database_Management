from Tkinter import *
import MySQLdb
import os
import time
import datetime
counter = 0
def ch():
	os.system('python /home/linaro/project/security_login_page2.py &')
	close(master)

def ex():
	os.system('python /home/linaro/project/home.py &')
	close(master)

def show_entry_fields():
	Label(master, text="                         ").grid(column=5, row=6)
	global counter
	usr = e1.get()
	pwd = e2.get()
	e1.delete(0,END)
	e2.delete(0,END)
	db = MySQLdb.connect("localhost","root","root","testdb" )
	cursor = db.cursor()
	cursor.execute ("select username, password from security_login")
	data = cursor.fetchall()
	cursor.close ()
        print data
	a = len(data)
	s = 1
	for i in range(0,a):
		if(usr == data[i][0]):
			s = 0
			if(pwd == data[i][1]):
				Label(master, text="     login succesful                  ",fg="green").grid(column=5,row=6)
				counter=0
				now = datetime.datetime.now()
				log_time= str(now)
				b={'name':usr,'log_time':log_time}
				cmd =  "INSERT INTO log (username,log_time,result,type) values('"+ b.get('name') +"','" + b.get('log_time') + "','success','security')"
				db = MySQLdb.connect("localhost","root","root","testdb")
				cursor = db.cursor()
				lab=""
				cursor.execute(cmd)
				db.commit()
				db.close()
				cursor.close()
				Button(master, text='editing options', command=ch).grid(row=6, column=4)
				Button(master, text='logout', command=ex).grid(row=7, column=4)
			else:
				counter = counter+1
				lab="incorrect password for "+str(counter)+" times "
				Label(master, text=lab,fg="red").grid(column=5,row=6)
				print counter
				now = datetime.datetime.now()
				log_time= str(now)
				b={'name':usr,'log_time':log_time}
				cmd =  "INSERT INTO log (username,log_time,result) values('"+ b.get('name') +"','" + b.get('log_time') + "','incorrect','security')"
				db = MySQLdb.connect("localhost","root","root","testdb")
				cursor = db.cursor()
				cursor.execute(cmd)
				db.commit()
				db.close()
				cursor.close()
		if(counter==3):
			Label(master, text="you have entered wrong password more than 3 times. you are blocked for 30 seconds",fg="red").grid(column=5)
			os.system("python /home/linaro/project/block.py &")
			counter=0
	if(s != 0):
		print("Login failed")
		Label(master, text="     no such user exists           ",fg="red").grid(column=5,row=6)
		log_time= str(datetime.now())
		b={'name':usr,'log_time':log_time}
		cmd =  "INSERT INTO log (username,log_time,result) values('"+ b.get('name') +"','" + b.get('log_time') + "','failed','security')"
		db = MySQLdb.connect("localhost","root","root","testdb")
		cursor = db.cursor()
		cursor.execute(cmd)
		db.commit()
		db.close()
		cursor.close()
def close(root):
	root.destroy()

def quit():
#	os.system('python home.py &')
	close(master)

master = Tk()
master.attributes("-fullscreen", True)
Label(master, text="                              ").grid(column=1, row=1)
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
b=Button(master)
photo1=PhotoImage(file='/home/linaro/project/security_login.gif')
b.config(image=photo1,width="250",height="300")
b.grid(row = 1, column = 4)


Label(master, text="First Name").grid(row=3,column=2)
Label(master, text="Last Name").grid(row=4,column=2)

e1 = Entry(master)
e2 = Entry(master,show="*")

e1.grid(row=3, column=4)
e2.grid(row=4, column=4)

Button(master, text='Quit', command=ex).grid(row=5, column=4)
Button(master, text='enter', command=show_entry_fields).grid(row=5, column=5)

mainloop( )