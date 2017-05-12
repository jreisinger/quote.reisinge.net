from flask import Flask
from subprocess import Popen, PIPE

app = Flask(__name__)

myquote = '/opt/quote/myquote'

@app.route('/')
def quote():
    cmd  = [ myquote, '-w' ]
    p = Popen(   cmd,
                 stdout = PIPE, 
                 stdin  = PIPE, 
                 stderr = PIPE
              )
    out, err = p.communicate()
    return out
