# coding: utf-8

# Webserverfunktionaliteten kombineres med ping-koden fra sidste gang
# SimpleHTTPServer lader os lave en webserver
import SimpleHTTPServer
# vi importerer Socket Server for at kunne lave en TCP server
import SocketServer
import time
# vi importerer Thread fra threading så vi kan lave en tråd/Thread
# Ved at bruge Thread kan vi have webserveren kørende i baggrunden
from threading import Thread
import subprocess
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

DEVNULL = open(os.devnull, 'wb')

# listen af servers udvides til at indeholde status også.
servers=[["10.0.1.1", 23, 'inactive'], ["10.0.1.2", 24,'inactive'], ["10.0.1.3",25,'inactive']]


PORT = 8000

# vi laver en Simple http server (default request handler) variable
# SimpleHTTPRequest handleren "servicerer" de html filer der findes i programfolderen
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# vi laver en TCP server på port 8000, og siger at "handler" skal processere indkommende requests
httpd = SocketServer.TCPServer(("", PORT), Handler)

# Vi sætter 'ping'-koden fra dag 2 ind i vores separate tråd
def readinput():
	while True:
		for ip in servers:
			result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip[0]], stdout=DEVNULL, stderr=DEVNULL).wait()
			if result:
	  			print ip[0], "inactive"
	  			# vi gemmer status
	  			ip[2] = 'inactive'
	  			GPIO.output(ip[1], 0)
			else:
				print ip[0], "active"
				# vi gemmer status
	  			ip[2] = 'active'
	  			GPIO.output(ip[1], 1)
	  		time.sleep(2)

# Vi opretter tråden 't' og putter vores 'readinput'-funktion
# ind i den
t = Thread(target=readinput)
# Denne linie gør at vi kan afslutte tråden når der trykkes CTRL-C
t.daemon = True
t.start()

print "serving at port", PORT
# vi laver en uendelig løkke der håndterer indkommende http requests
while True:
	httpd.handle_request()
