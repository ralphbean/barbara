# -*- coding: utf-8 -*-
"""Setup the barbara application"""

import logging
from tg import config
from barbara import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup barbara here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
