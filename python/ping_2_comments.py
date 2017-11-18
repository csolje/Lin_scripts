# coding: utf-8
import subprocess
# Ved at importere os-biblioteket kan åbne en fil.
import os

# vi åbner filen os.devnull. Dev null er en fil som ignorere al data (sort hul)
DEVNULL = open(os.devnull, 'wb')

# Vi laver et array af strenge (de forskellige IPs)
servers=["10.0.1.1", "10.0.1.2", "10.0.1.3"]

# For hver plads i vores array afvikler vi koden, for løkken sætter "ip" lig med en streng i array'et servers
# for hvert gennemløb
for ip in servers:
# vi tilføjer 2 parametere på Popen som sender tekst output fra ping til "dev null" istedet for skærmen
	result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=DEVNULL, stderr=DEVNULL).wait()
	if result:
		print ip, "inactive"
	else:
		print ip, "active"
