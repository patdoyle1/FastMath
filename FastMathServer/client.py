#!/usr/bin/python           # This is client.py file

import socket, os, sys               # Import socket module


def parse_output(res, question):
	foundAns = False
	for pod in res:
		if foundAns is True:
			return pod.text
		foundAns = True

def parse_question(q):
	q = q.replace('"', '^')
	return q


size = 512

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port)) # connects to the server


fname = os.system(sys.argv[1]) # this is the picture being passed in
s.send(fname) #sends the picture to the server

print s.recv(1024)

s.close                     # Close the socket when done