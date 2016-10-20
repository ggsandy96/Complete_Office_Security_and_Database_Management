import signal
import time
login=0
def signal_handler1(signal, frame):
	global login
	if(login==0):
		import RPi.GPIO as GPIO
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(18, GPIO.OUT)
		GPIO.output(18, GPIO.HIGH)
		time.sleep(10)
		GPIO.output(18, GPIO.LOW)
		print "alarm"

def signal_handler2(signal, frame):
	global login
	login=1
	time.sleep(30)
	login=0

signal.signal(signal.SIGUSR1, signal_handler1)
signal.signal(signal.SIGUSR2, signal_handler2)
while(1):
	text=0
