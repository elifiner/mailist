#!/usr/bin/env python
from bottle import *

class dictobj(dict):
    __getattr__ = dict.__getitem__

@route('/')
def index():
    return template('index')

@route('/', method='POST')
def generate():
    messages = []
    for i in range(10):
        messages.append(dictobj(address='adr{}'.format(i+1), subject='subj{}'.format(i+1), text='text{}'.format(i+1)))
    return template('messages', messages=messages)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
