# -*- coding: UTF-8 -*- 
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

#建立一个socket对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)

#这是客户处理线程
def handle_client(client_socket):

    # 打印出客户端发送得到的内容
    request = client_socket.recv(1024)

    print "[*] Received: %s" % request

    #返还一个数据包
    client_socket.send("ACK!")
    client_socket.close()

while True:

    client,addr = server.accept()
    #for i in addr:
    #    print i

    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])

    #挂起客户端线程，处理传入的数据
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()

