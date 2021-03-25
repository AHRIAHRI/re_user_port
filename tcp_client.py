#!/usr/bin/env python
import sys
from socket import *
import threading
import time

HOST="127.0.0.1"
PORTS=sys.argv[1:]
localPort=40000
BUFSIZE=1024

def create_sockets(v_ports):
    list_socket = []
    for port in v_ports:
        t_client = socket(AF_INET,SOCK_STREAM)
        t_client.setsockopt(SOL_SOCKET,SO_REUSEPORT, 1)
        t_client.bind(('',localPort))
        list_socket.append({'port':int(port),'socket':t_client})
    return list_socket


def create_tcp_client(info):
    info['socket'].connect(( HOST,info['port']))
    n = 0
    while 1 :
        data = 'myport is %s ,send %s' %(info['port'],n)
        info['socket'].send(data)
        data = info['socket'].recv(BUFSIZE)
        print "server addr is %s:%s ,my addr is %s" %(HOST,info['port'],data)
        n = n +1
        time.sleep(1)
        if n == 20 : break

tlist = []
for x in create_sockets(PORTS):
    t = threading.Thread(target=create_tcp_client,args=(x,))
    tlist.append(t)
for t1 in tlist:
    t1.setDaemon(True)
    t1.start()

for t1 in tlist:
    t1.join()