from flask import Flask
from flask import request
app = Flask(__name__)
app.config['DEBUG'] = True
from wolframrequest import wolfram
app_id = "642Q4J-E5E9RP93XH"
import wolframalpha


# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/hi')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/')
def makequery():
    #query_string = request.query_string
    client = wolframalpha.Client(app_id)
    thequery = "derive x^2"
    res = client.query(thequery)
    deriv = "deriv"
    integral = "integr"
    if deriv in thequery or integral in thequery:
	for pod in res.pods:
	    return(pod.text)
    else:   
	return(next(res.results).text)


    #return(next(res.results).text)
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
