#!/usr/bin/env python
from bottle import route, run, template, static_file

@route('/')
def index():
    return template('index')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

if __name__ == '__main__':
    run(host='localhost', port=8080, reload=True)
