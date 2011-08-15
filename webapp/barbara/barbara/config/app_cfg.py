# -*- coding: utf-8 -*-
"""
Global configuration file for TG2-specific settings in barbara.

This file complements development/deployment.ini.

Please note that **all the argument values are strings**. If you want to
convert them into boolean, for example, you should use the
:func:`paste.deploy.converters.asbool` function, as in::
    
    from paste.deploy.converters import asbool
    setting = asbool(global_conf.get('the_setting'))
 
"""

from tg.configuration import AppConfig

import barbara
from barbara import model
from barbara.lib import app_globals, helpers 

base_config = AppConfig()
base_config.renderers = []

base_config.package = barbara

#Enable json in expose
base_config.renderers.append('json')
#Set the default renderer
base_config.default_renderer = 'mako'
base_config.renderers.append('mako')


base_config.use_sqlalchemy=False
base_config.use_transaction_manager=False
base_config.auth_backend=None
base_config.use_toscawidgets=False

