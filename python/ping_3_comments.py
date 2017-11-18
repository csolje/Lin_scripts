# coding: utf-8
import subprocess
import os
# Vi inkluderer time-biblioteket ligesom sidst
import time

DEVNULL = open(os.devnull, 'wb')

servers=["10.0.1.1", "10.0.1.2", "10.0.1.3"]

# Vi putter vores kode i en while-løkke. Denne vil altid være True i vores kode her
# og derfor vil koden loope uendeligt, men med 2 sekunders mellemrum jf. nederste linje
while True:
	for ip in servers:
		result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=DEVNULL, stderr=DEVNULL).wait()
		if result:
			print ip, "inactive"
		else:
			print ip, "active"
	time.sleep(2)
