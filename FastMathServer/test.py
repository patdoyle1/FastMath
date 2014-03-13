#from __future__ import unicode_literals
import wolframalpha
import sys
import os
import subprocess

app_id = 'TGR8PR-V28TUUGJWY'
"App ID for testing this project. Please don't use for other apps."

def parse_question(q):
	q = q.replace('"', '^')
	return q

def parse_output(res, question):
	foundAns = False
	for pod in res:
		if foundAns is True:
			return pod.text
		foundAns = True

if __name__ == "__main__":
	imageInputFileName = "image-tests\\testMultiply.PNG"
	tesseractQuery = 'Tesseract-OCR\\tesseract.exe ' + imageInputFileName + ' input' # this command will be different for macs and unix systems
	os.system(tesseractQuery) # send command to terminal 
	inputFileName = "input.txt" # name of file which holds the query in text form 
	question = open(inputFileName).readline().strip()
	question = parse_question(question)
	client = wolframalpha.Client(app_id) 
	res = client.query(question) # send query to wolfram 
	#print(parse_output(res, question)) # prints the final output to the question (alternatives avalible, but for debugging we'll stick with this)
	for pod in res:
		print pod.text
	
	


		