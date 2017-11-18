# coding: utf-8

# SimpleHTTPServer lader os lave en webserver
import SimpleHTTPServer
# vi importerer Socket Server for at kunne lave en TCP server
import SocketServer

# Vi angiver, at vi vil bruge port 8000 til kommunikationen
PORT = 8000

# vi laver en Simple http server (default request handler) variable
# SimpleHTTPRequest handleren "servicerer" de html filer der findes i programfolderen
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# vi laver en TCP server på port 8000, og siger at "handler" skal processere indkommende requests
httpd = SocketServer.TCPServer(("", PORT), Handler)

# Vi udskriver den port webserveren er på, i terminalen
print "serving at port", PORT

# vi laver en uendelig løkke der håndterer indkommende http requests
while True:
	httpd.handle_request()
