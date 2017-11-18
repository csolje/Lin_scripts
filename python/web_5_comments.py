# coding: utf-8
#
# Dette eksempel viser hvordan man sikrer sig ikke at få "læsefejl" af index.html
# Dette gøre ved at skrive index.html-indholdet direkte til browseren istedet for en fil
# Dette gøres ved at implementere en request handler istedet for at bruge "default handleren"
import SimpleHTTPServer
import SocketServer
import time
from threading import Thread
import subprocess
import os
# Vi importerer BaseHTTPRequestHandler
from BaseHTTPServer import BaseHTTPRequestHandler
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

DEVNULL = open(os.devnull, 'wb')

# Listen udvides til også at indeholde status
servers=[["10.0.1.1", 23, 'inactive'], ["10.0.1.2", 24,'inactive'], ["10.0.1.3",25,'inactive']]


PORT = 8000
# en request handler lavet ved at lave en class baseret på BaseHTTPRequestHandler
# i denne class have vi en go_GET funktion som bliver kaldt når en browser vil
# hente et object (index.html)
# her skriver vi så status af de 3 servers
class myHandler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.0"
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write('<html>\n')
		self.wfile.write('<head>')
		self.wfile.write('<title>RPi web</title>')
		self.wfile.write('<meta http-equiv="refresh" content="5"/>')
		self.wfile.write('</head>\n')
		self.wfile.write('<body>\n')
		for ip in servers:
	  		self.wfile.write(ip[0] + " " + ip[2] +"</br>")

		self.wfile.write('</body>\n')
		self.wfile.write('</html>\n')
		return

# når vi opretter tcp serveren beder vi den nu om at bruge vores nye handler
httpd = SocketServer.TCPServer(("", PORT), myHandler)

# I vores særskilte tråd sørger vi for at opdatere listen hver 2. sekund.
def readinput():
	while True:
		for ip in servers:
			result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip[0]], stdout=DEVNULL, stderr=DEVNULL).wait()
			if result:
	  			print ip[0], "inactive"
	  			ip[2] = 'inactive'
	  			GPIO.output(ip[1], 0)
			else:
	  			print ip[0], "active"
	  			ip[2] = 'active'
	  			GPIO.output(ip[1], 1)
	  	time.sleep(2)

t = Thread(target=readinput)
t.daemon = True
t.start()

print "serving at port", PORT
while True:
	httpd.handle_request()
