#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return '<h1>Hello World!</h1>', 200

if __name__ == '__main__':
    app.run()
    
