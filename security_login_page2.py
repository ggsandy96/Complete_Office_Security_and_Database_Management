from Tkinter import *
import MySQLdb
import os

def cc():
	os.system('sudo omxplayer -o hdmi --win "10 10 1280 720" rtsp://admin:admin@192.168.0.10')
	Button(master, text='exit the cctv feed', command=ki).grid(row=8, column=9)

def ki():
	os.system('sudo /home/linaro/project/kill_omx.sh')
	print "hello"
	Button(master, text='      view cctv feed', command=cc).grid(row=8, column=9)

def ex():
	os.system('python /home/linaro/project/home.py &')
	close(master)

def vl():
	db = MySQLdb.connect("localhost","root","root","testdb" )
	cursor = db.cursor()
	cursor.execute ("select * from log")
	lst = cursor.fetchall()
	lst=zip(*lst)
	cursor.close ()
	label=Label(master,text="username").grid(column=2,row=4)
	label=Label(master,text="logged time").grid(column=3,row=4)
	label=Label(master,text="result").grid(column=4,row=4)
	label=Label(master,text="type").grid(column=5,row=4)          
	label=Label(master,text="\n".join(map(str,lst[0]))).grid(column=2,row=5)
	label=Label(master,text="\n".join(map(str,lst[1]))).grid(column=3,row=5)
	label=Label(master,text="\n".join(map(str,lst[2]))).grid(column=4,row=5)
	label=Label(master,text="\n".join(map(str,lst[3]))).grid(column=5,row=5)

def ud():
	db = MySQLdb.connect("localhost","root","root","testdb" )
	cursor = db.cursor()
	cursor.execute ("select * from details")
	lst = cursor.fetchall()
	lst=zip(*lst)
	cursor.close ()
	label=Label(master,text="name").grid(column=2,row=4)
	label=Label(master,text="email").grid(column=3,row=4)
	label=Label(master,text="phone").grid(column=4,row=4)
	label=Label(master,text="office").grid(column=5,row=4)
        label=Label(master,text="employee id").grid(column=6,row=4)          
	label=Label(master,text="\n".join(map(str,lst[0]))).grid(column=2,row=5)
	label=Label(master,text="\n".join(map(str,lst[1]))).grid(column=3,row=5)
	label=Label(master,text="\n".join(map(str,lst[2]))).grid(column=4,row=5)
	label=Label(master,text="\n".join(map(str,lst[3]))).grid(column=5,row=5)
	label=Label(master,text="\n".join(map(str,lst[3]))).grid(column=6,row=5)


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
Label(master, text="                              ").grid(column=7, row=2)
Label(master, text="                              ").grid(column=8, row=2)
Label(master, text="                              ").grid(column=9, row=2)


wel = "hello security"
Label(master, text=wel).grid(row=3,column=1)
Button(master, text='view log', command=vl).grid(row=6, column=9)
Button(master, text='logout', command=ex).grid(row=3, column=9)
Button(master, text='view user details', command=ud).grid(row=7, column=9)
Button(master, text='      view cctv feed', command=cc).grid(row=8, column=9)

mainloop( )