#from __future__ import unicode_literals
import wolframalpha
import sys

app_id = 'TGR8PR-V28TUUGJWY'
"App ID for testing this project. Please don't use for other apps."

def parse_question(q):
	q = q.replace('"', '^')
	return q

if __name__ == "__main__":
	output = str(sys.argv[1])
	question = open(output).readline().strip()
	question = parse_question(question)
	
	client = wolframalpha.Client(app_id)
	res = client.query(question)
	for pod in res:
		print pod.text


		