import time
import subprocess
import os

def delay(text,delay):
	for char in text:
		print(char, end="",flush=True)
		time.sleep(delay)

delay('''	
		▄▄▄  ▄▄▄     ▄▄     ▄▄▄   ▄▄     ▄▄     ▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄ 
	        ███  ███    ████    ███   ██    ████    ██▀▀▀▀▀▀  ██▀▀▀▀▀▀ 
	 	████████    ████    ██▀█  ██    ████    ██        ██       
	 	██ ██ ██   ██  ██   ██ ██ ██   ██  ██   ███████   ███████  
	 	██ ▀▀ ██   ██████   ██  █▄██   ██████   ██        ██       
	 	██    ██  ▄██  ██▄  ██   ███  ▄██  ██▄  ██        ██▄▄▄▄▄▄ 
	 	▀▀    ▀▀  ▀▀    ▀▀  ▀▀   ▀▀▀  ▀▀    ▀▀  ▀▀        ▀▀▀▀▀▀▀▀ 
	 	                                                 
	 	''',0.01)
delay('''\\Booting...Manafe says your system is on fire..''',0.5)
time.sleep(1.5)
subprocess.call(["cacafire"])
delay("Manafe will be taking over the system now..Sayonara..",0.03)
os.system("shutdown -h now")



