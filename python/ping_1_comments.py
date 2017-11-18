# coding: utf-8

# Vi importerer subprocess-biblioteket, så vi kan afvikle et ekternt program .
import subprocess

# Vi sætter en variabel 'ip' til strengen '10.0.1.1'
ip="10.0.1.1"
# vha. funktionen 'Popen' i subprocess-biblioteket
# pinger vi variablen 'ip' og venter på et svar...MADS
result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip]).wait()
# Hvis vi får et svar på vores ping returneres status koden 0 og vi ved at serveren er i live
# Hvis ikke, så er den inaktiv.
if result:
	print ip, "inactive"
else:
	print ip, "active"
