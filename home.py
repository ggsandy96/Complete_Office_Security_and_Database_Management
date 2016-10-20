from Tkinter import *
import os

def ex():
	close(master)

def admin_login():
	print 'hello'
	os.system('python /home/linaro/project/admin_login.py &')
	close(master)
def user_login():
	print 'hello'
	os.system('python /home/linaro/project/user_login.py &')
	close(master)
def head_login():
	print 'hello'
	os.system('python /home/linaro/project/hoo_login.py &')
	close(master)
def security_login():
	print 'hello'
	os.system('python /home/linaro/project/security_login.py &')
	close(master)

def close(root):
	root.destroy()

master = Tk()
master.attributes("-fullscreen", True)

wel=Button(master)
a=Button(master, command=admin_login)
b=Button(master, command=user_login)
c=Button(master, command=head_login)
d=Button(master, command=security_login)

wel_pic=PhotoImage(file='/home/linaro/project/welcome.gif')
photo0=PhotoImage(file='/home/linaro/project/admin_login.gif')
photo1=PhotoImage(file='/home/linaro/project/user_login.gif')
photo2=PhotoImage(file='/home/linaro/project/head_login.gif')
photo3=PhotoImage(file='/home/linaro/project/security_login.gif')

wel.config(image=wel_pic,width="1400",height="400")
a.config(image=photo0,width="250",height="300")
b.config(image=photo1,width="250",height="300")
c.config(image=photo2,width="250",height="300")
d.config(image=photo3,width="250",height="300")

wel.grid(row=1, column=0, columnspan = 4)
a.grid(row = 2, column = 0)
b.grid(row = 2, column = 1)
c.grid(row = 2, column = 2)
d.grid(row = 2, column = 3)

a0=Button(master, text='admin login', command=admin_login).grid(row=3, column=0)
a1=Button(master, text='user login', command=user_login).grid(row=3, column=1)
a2=Button(master, text='head login', command=head_login).grid(row=3, column=2)
a3=Button(master, text='security login', command=security_login).grid(row=3, column=3)
a4=Button(master, text='Close', command=ex).grid(row=1, column=3)

master.mainloop()