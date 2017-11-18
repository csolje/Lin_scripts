# coding: utf-8
import subprocess
import os
import time
# Vi inkluderer GPIO-biblioteket, for at få adgang til GPIO-benene på Raspberry Pi
# Husk, at man altid skal afvikle via kommandolinjen med 'sudo', når man vil have adgang til GPIO
import RPi.GPIO as GPIO

#vi sætter hvilket GPIO mode vi bruger - BCM
GPIO.setmode(GPIO.BCM)

# Ben 23,24,25 sættes som output
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

DEVNULL = open(os.devnull, 'wb')

#vi udvider arrayet med en dimension der indholder ben'et vi skal bruge til at indikere aktiv/inaktiv
servers=[["10.0.1.1", 23], ["10.0.1.2", 24], ["10.0.1.3",25]]

while True:
	for ip in servers:
# da severs arrayet nu er 2 dimensionelt skal vi indikere hvilket vi bruger ip[0] gør at vi peger korrekt
		result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip[0]], stdout=DEVNULL, stderr=DEVNULL).wait()
		if result:
# Ping returnere en status kode. hvis den er 0 er mindst en response hørt.
			print ip[0], "inactive"
# Vi sætter GPIO til 0/lav hvis serveren er inaktiv
# læg mærke til at her bruger vi ip[1] for at udlæse ben'et fra arrayet.
			GPIO.output(ip[1], 0)
		else:
# result er 0 og vi sætter GPIO til 1/høj
			print ip[0], "active"
			GPIO.output(ip[1], 1)
	time.sleep(2)
