from flask import Flask
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
    client = wolframalpha.Client(app_id)
    res = client.query('2+2')
    return(next(res.results).text)
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
