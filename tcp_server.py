#!/usr/bin/env python

from socket import *
from time import ctime
import sys

HOST=""
PORT=int(sys.argv[1])
BUFSIZE=1024
ADDR=(HOST,PORT)

# server
t_server = socket(AF_INET,SOCK_STREAM)
t_server.bind(ADDR)
t_server.listen(5)

try:
    while 1:
        print "wait connent ction"
        t_client , c_addr = t_server.accept()
        print 'accept from:',c_addr
        while 1:
            data = t_client.recv(BUFSIZE)
            if not data:
                break
            t_client.send('[server->] my addr is  %s' %(str(c_addr)))
finally:
    t_server.close()


