#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socketserver import TCPServer
from http.server import SimpleHTTPRequestHandler


HOST = '0.0.0.0'
PORT = 8000

SimpleHTTPRequestHandler.extensions_map = {
    '.html': 'text/html',
    '.sh': 'text/x-sh',
    '.js': 'application/javascript',
    '.pac': 'application/x-ns-proxy-autoconfig',
    '': 'application/octet-stream',
}

server = TCPServer((HOST, PORT), SimpleHTTPRequestHandler)

if __name__ == '__main__':
    print('pac server running at {}:{}'.format(HOST, PORT))
    server.serve_forever()
