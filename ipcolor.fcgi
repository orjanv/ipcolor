#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from ipcolor import app

if __name__ == '__main__':
  WSGIServer(app, bindAddress = '/tmp/ipcolor-fcgi.sock').run()
