import subprocess
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

DEVNULL = open(os.devnull, 'wb')

servers = [["8.8.8.8", 23], ["8.8.4.4", 24], ["159.20.6.38", 25]]

while True:
	for ip in servers:
		result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip[0]], stdout=DEVNULL, stderr=DEVNULL).wait()
		if result:
			print ip, "inactive"
			GPIO.output(ip[1], 0)

		else:
			print ip, "active"
			GPIO.output(ip[1], 1)

	time.sleep(2)
	#GPIO.cleanup()
