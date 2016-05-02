#!/usr/bin/python

import CGIHTTPServer

try:
    CGIHTTPServer.test()
except(KeyboardInterrupt):
    print "[+] Shutting down server..."
