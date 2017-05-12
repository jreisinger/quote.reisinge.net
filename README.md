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

    sudo mkdir /opt/quote
    cd /opt/quote
    sudo git clone git@github.com:jreisinger/quote.reisinge.net.git
    sudo mv quote.reisinge.net/* .
    sudo rm -rf quote.reisinge.net
    pip install -r requirements.txt
    sudo wget https://raw.githubusercontent.com/jreisinger/dotfiles/master/bin/myquote
    sudo chmod u+x myquote
    sudo chown -R http: /opt/quote
    echo "copy config(s) from etc"
