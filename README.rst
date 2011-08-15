barbara streisand
-----------------

Installation
------------

Follow these simple steps::

  $ sudo yum install espeak
  $ mkvirtualenv barbara
  $ git clone git://github.com/ralphbean/barbara.git
  $ cd barbara/webapp/barbara
  $ python setup.py develop
  $ paster serve development.ini  # Point your browser to http://localhost:8080


