#!/usr/bin/env python

from flask import Flask

web_app = Flask(__name__)

@web_app.route('/')
def helloworld():
    return '<h1>Hello World!</h1>', 200
