Setup

    # Do once
    sudo pip install virtualenv
    virtualenv venv # create your own environment

Develop

    . venv/bin/activate
    pip install -r requirements.txt
    
    # If you installed something new via pip
    pip freeze > requirements.txt
    
    deactivate

Run

    export FLASK_APP=quote.py
    flask run [--host=0.0.0.0]

Install

    mkdir /opt/quote
    cd /opt/quote
    wget https://github.com/jreisinger/dotfiles/blob/master/bin/myquote
