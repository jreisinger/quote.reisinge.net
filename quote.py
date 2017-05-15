from flask import Flask, render_template
from subprocess import Popen, PIPE

app = Flask(__name__)

myquote = '/opt/quote.reisinge.net/myquote'

@app.route('/')
def quote():
    cmd  = [ myquote, '-a' ]
    p = Popen(   cmd,
                 stdout = PIPE, 
                 stdin  = PIPE, 
                 stderr = PIPE
              )
    out, err = p.communicate()
    out = str(out.decode('utf-8'))
    (quote, url, link) = out.split('|')
    #return out
    return render_template('layout.html', quote=quote, url=url, link=link)
