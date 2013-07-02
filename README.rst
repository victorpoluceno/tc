TC
==

Bootstrap::

    cd /vagrant
    sh setup.sh
    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt

Running::

    cd /vagrant
    python app.py


LESS
----

To code and have live less compile download an use `SimpleLESS <http://wearekiss.com/simpless>`_.


TODO
----

- Add nginx and uwsgi support with supervisor
- Create a fabric script for automated deploy
