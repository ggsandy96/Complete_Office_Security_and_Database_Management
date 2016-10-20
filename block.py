import time
import MySQLdb
db = MySQLdb.connect("localhost","root","root","testdb" )
cursor = db.cursor()
cursor.execute ("select username from log")
log = cursor.fetchall()
block=log[-1]
print block
block=block[0]
block=str(block)
print block
del log
cursor.execute ("select username,password from login")
data= cursor.fetchall()
print data
a = len(data)
for i in range(0,a):
	print "entered loop"
	if(block == data[i][0]):
		pas=data[i][1]
print pas
cmd="delete from login where username='"+block+"'"
print cmd
cursor.execute (cmd)
db.commit()
time.sleep(30)
cmd="INSERT INTO login (username,password) values('"+block+"','"+pas+"')"
cursor.execute (cmd)
db.commit()
cursor.close ()