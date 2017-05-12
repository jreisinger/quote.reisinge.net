Develop

    # Do once
    sudo pip install virtualenv
    virtualenv venv # create your own environment

    . venv/bin/activate
    pip install -r requirements.txt
    
    # If you installed something new via pip
    pip freeze > requirements.txt
    
    deactivate

    # Run
    export FLASK_APP=quote.py
    flask run [--host=0.0.0.0]

Deploy

    cd /opt
    sudo git clone git@github.com:jreisinger/quote.reisinge.net.git
    . venv/bin/activate # if this doesn't work see above
    pip install -r requirements.txt
    deactivate
    sudo wget https://raw.githubusercontent.com/jreisinger/dotfiles/master/bin/myquote
    sudo chmod u+x myquote
    sudo chown -R http: /opt/quote
    echo "copy config(s) from etc"
