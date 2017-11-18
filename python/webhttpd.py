import SimpleHTTPServer
import SocketServer
import time
from threading import Thread
import subprocess
import os
from BaseHTTPServer import BaseHTTPRequestHandler
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

DEVNULL = open(os.devnull, 'wb')

servers=[["8.8.8.8", 23, 'inactive'], ["8.8.4.4", 24, 'inactive'], ["159.20.6.38", 25, 'inactive']]

PORT = 8000

class myHandler(BaseHTTPRequestHandler):
	protocol_version = "HTTP/1.0"
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write('<html>')
		self.wfile.write('<head>')
		self.wfile.write('<title>RPi Web</title>')
		self.wfile.write('<meta http-equiv="refresh" content="5">')
		self.wfile.write('</head>\n')
		self.wfile.write('<body>\n')
		for ip in servers:
			self.wfile.write(ip[0] + " " + ip[2] + "<br />")

		self.wfile.write('</body>\n')
		self.wfile.write('</html>\n')
		return

httpd = SocketServer.TCPServer(("", PORT), myHandler)

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

print "Serving at port", PORT
while True:
	httpd.handle_request()


# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# httpd = SocketServer.TCPServer(("", PORT), Handler)

# def readinput():
# 	while True:
# 		for ip in servers:
# 			result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip[0]], stdout=DEVNULL, stderr=DEVNULL).wait()
# 			if result:
# 				print ip[0], "inactive"
# 				ip[2] = 'inactive'
# 				GPIO.output(ip[1], 0)
# 			else:
# 				print ip[0], "active"
# 				ip[2] = 'active'
# 				GPIO.output(ip[1], 1)
# 		fil = open('index.html', 'w')
# 		fil.write('<!DOCTYPE html>\n')
# 		fil.write('<html>')
# 		fil.write('<head>')
# 		fil.write('<title>RPi Web</title>')
# 		fil.write('<meta http-equiv="refresh" content="5" />\n')
# 		fil.write('</head>\n')
# 		fil.write('<body>\n')
# 		for ip in servers:
# 			fil.write(ip[0] + " " + ip[2] + "<br />")
# 		fil.write('</body>')
# 		fil.write('</html>')
# 		fil.close()
# 		time.sleep(2)

# t = Thread(target=readinput)
# t.daemon = True
# t.start()

# print "Serving at port", PORT
# while True:
# 	httpd.handle_request()
