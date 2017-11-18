# coding: utf-8

# SimpleHTTPServer lader os lave en webserver
import SimpleHTTPServer
# vi importerer Socket Server for at kunne lave en TCP server
import SocketServer
# Vi importerer time, for at kunne bruge sleep-funktionen
import time
# vi importerer Thread fra threading så vi kan lave en tråd/Thread
# Ved at bruge Thread kan vi have webserveren kørende i baggrunden
from threading import Thread

PORT = 8000

# vi laver en Simple http server (default request handler) variable
# SimpleHTTPRequest handleren "servicerer" de html filer der findes i programfolderen
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# vi laver en TCP server på port 8000, og siger at "handler" skal processere indkommende requests
httpd = SocketServer.TCPServer(("", PORT), Handler)

#Vi definerer en funktion 'readinput' der ikke har nogen parametre.
def readinput():
# Vi udskriver 'thread 2' hvert 2. sekund, for at se,
# at vores anden tråd kører
	while True:
		time.sleep(2)
		print "thread 2"

# Vi opretter tråden 't' og putter vores 'readinput'-funktion
# ind i den
t = Thread(target=readinput)
# Denne linie gør at vi kan afslutte tråden når der trykkes CTRL-C
t.daemon = True
# Tråden startes
t.start()

print "serving at port", PORT
# vi laver en uendelig løkke der håndterer indkommende http requests
while True:
	httpd.handle_request()
