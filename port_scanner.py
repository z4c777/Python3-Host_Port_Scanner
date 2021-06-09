#!/usr/bin/python3

from socket import gethostbyname, gethostname, AF_INET, SOCK_STREAM, socket

HOST = gethostbyname(gethostname())
PORTS = 65535
for port in range(PORTS):
	with socket(AF_INET, SOCK_STREAM) as sock:
		try:
			sock.bind((HOST, port))
		except OSError:
			print(f"Port: {port} is open")
