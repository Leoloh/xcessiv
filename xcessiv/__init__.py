from __future__ import absolute_import, print_function,\
    nested_scopes, generators, division, with_statement, unicode_literals
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')


import xcessiv.views
