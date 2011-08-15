barbara streisand
-----------------

Installation
------------

Follow these steps::

  $ sudo yum install espeak libyaml-devel gstreamer
  $ mkvirtualenv barbara
  $ pip install \
        PyYAML \
        http://pypi.python.org/packages/source/n/nltk/nltk-2.0.1rc1.tar.gz
  $ git clone git://github.com/ralphbean/barbara.git
  $ cd barbara/webapp/barbara
  $ python setup.py develop
  $ paster serve development.ini  # Point your browser to http://localhost:8080


