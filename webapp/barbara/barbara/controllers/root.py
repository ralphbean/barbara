# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, request, redirect
from pylons.i18n import ugettext as _, lazy_ugettext as l_
from hashlib import md5

import subprocess
import itertools
import string
import sys

from curses.ascii import isdigit
from nltk.corpus import cmudict

cmud = cmudict.dict()

def nsyl(word):
    return [len(list(y for y in x if isdigit(y[-1])))
            for x in cmud[word.lower()]]


from barbara.lib.base import BaseController

from barbara.controllers.error import ErrorController


__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the barbara application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    # TODO -- disable this in production
    error = ErrorController()

    @expose('barbara.templates.index')
    def index(self, n=4):
        """Handle the front-page."""
        return dict(page='index')

    @expose()
    def duckpunch(self, words, submit):
        words = words.split()

        # Strip punctuation
        exclude = set(string.punctuation)
        words = [''.join(ch for ch in word if ch not in exclude) for word in words]

        n = min(self.count_syllables(words))
        if n != 4:
            redirect('/?n=%i' % n)

        tag = md5("-".join(words)).hexdigest()

        # Filename
        fname = tag + '.wav'
        # Fully qualified filename
        fqfname = '/'.join(__file__.split('/')[:-2] +
                           ['public', 'barbara', fname])

        # Create the .wav file
        subprocess.Popen(['espeak', '-w', fqfname, " ".join(words)])

        redirect('/barbara/' + fname)

    @expose('barbara.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    def count_syllables(self, words):
        """ Utility to count the syllables in a number of words """

        # Count syllables of each word.
        try:
            results = [nsyl(word) for word in words]
        except KeyError as e:
            print "** Unrecognized word.", str(e)
            sys.exit(1)

        # Upper and lower bound
        upper = sum([max(r) for r in results])
        lower = sum([min(r) for r in results])
        return [lower, upper]
