#from __future__ import unicode_literals
import wolframalpha
import sys
import os
import subprocess
import socket               # Import socket module

app_id = 'TGR8PR-V28TUUGJWY'
"App ID for testing this project. Please don't use for other apps."

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

requests = "inputs.txt" #potential way to store all of the requests that come in

def parse_output(res, question):
	foundAns = False
	for pod in res:
		if foundAns is True:
			return pod.text
		foundAns = True

def parse_question(q):
	q = q.replace('"', '^')
	return q



s.listen(5)                 # Now wait for client connection. (can only hold query of 5)
while True:
    c, addr = s.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    data = client_socet.recv(512)   # 512 is the number of bytes
        
        if __name__ == "__main__":
            imageInputFileName = open(data, 'rb')
            tesseractQuery = 'Tesseract-OCR\\tesseract.exe ' + imageInputFileName + ' input' # this command will also be different for unix systems
            os.system(tesseractQuery))) # send command to terminal
            question = subprocess.check_output(os.system(tesseractQuery))#sets question to whatever tesseract spits out
            
            parse_question(question)
            
            query = open('inputs.txt',w) #opens input and writes the question to it
            query.write(question "\n")
            query.close()
            
            client = wolframalpha.Client(app_id)
            res = client.query(question) # send query to wolfram
            res = parse_output(res,question)
            
            c.send(res)
    
    
    
    
    c.close()                # Close the connection














