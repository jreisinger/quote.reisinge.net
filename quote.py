from flask import Flask
from subprocess import Popen, PIPE
from os.path import expanduser, join

app = Flask(__name__)

@app.route('/')
def quote():
    home = expanduser("~")
    cmd  = [ join(home, 'bin', 'myquote'), '-w' ]
    p = Popen(   cmd,
                 stdout = PIPE, 
                 stdin  = PIPE, 
                 stderr = PIPE
              )
    out, err = p.communicate()
    return out
