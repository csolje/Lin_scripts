import time
from threading import Thread

def tester():
	print "test 1"
	time.sleep(2)
	print "test 2"


t = Thread(target=tester)
t.daemon = True
t.start()

while True:
	print("test for while")
	time.sleep(2)

