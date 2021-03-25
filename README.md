# re_user_port

> 启动一个18888的服务端
```bash
./tcp_server.py 18888 
```

> 再启动一个终端,启动一个18889的服务端
```bash
./tcp_server.py 18889
```

> 再启动一个客户端链接刚才的那两个服务器端口
```bash
./tcp_client.py 18888 18889
```

>观察输出