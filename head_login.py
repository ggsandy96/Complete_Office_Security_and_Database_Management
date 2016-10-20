from Tkinter import *
import MySQLdb
import os
import time
import datetime
counter = 0
def show_entry_fields():
#	os.system("python /home/pi/Desktop/practice/input_log.py &")
	global counter
	usr = e1.get()
	pwd = e2.get()
	e1.delete(0,END)
	e2.delete(0,END)
	db = MySQLdb.connect("localhost","root","root","testdb" )
	cursor = db.cursor()
	cursor.execute ("select username, password from hoa_login")
	data = cursor.fetchall()
	cursor.close ()
        print data
	a = len(data)
	s = 1
	for i in range(0,a):
		if(usr == data[i][0]):
			s = 0
			if(pwd == data[i][1]):
				print "login successful"
				counter=0
				now = datetime.datetime.now()
				log_time= str(now)
				b={'name':usr,'log_time':log_time}
				cmd =  "INSERT INTO log (username,log_time,result) values('"+ b.get('name') +"','" + b.get('log_time') + "','success')"
				db = MySQLdb.connect("localhost","root","root","testdb")
				cursor = db.cursor()
				cursor.execute(cmd)
				db.commit()
				db.close()
				cursor.close()
			else:
				print "incorrect password"
				counter = counter+1
				print counter
				now = datetime.datetime.now()
				log_time= str(now)
				b={'name':usr,'log_time':log_time}
				cmd =  "INSERT INTO log (username,log_time,result) values('"+ b.get('name') +"','" + b.get('log_time') + "','incorrect')"
				db = MySQLdb.connect("localhost","root","root","testdb")
				cursor = db.cursor()
				cursor.execute(cmd)
				db.commit()
				db.close()
				cursor.close()
		if(counter==3):
			time.sleep(30)
			counter=0
	if(s != 0):
		print("Login failed")
		log_time= str(datetime.now())
		b={'name':usr,'log_time':log_time}
		cmd =  "INSERT INTO log (username,log_time,result) values('"+ b.get('name') +"','" + b.get('log_time') + "','failed')"
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
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master,show="*")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='enter', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )