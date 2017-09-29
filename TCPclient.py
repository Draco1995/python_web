# -*- coding: UTF-8 -*- 
import socket

target_host = "0.0.0.0"
target_port = 9999
'''
#建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#链接客户端
client.connect((target_host,target_port))

#发送一些数据
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#接收一些数据
response = client.recv(4096)

print response
'''
def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        #连接到目标主机
        client.connect((target,port))

        if len(buffer):
            client.send(buffer)


        while True:
            recv_len = 1
            response = ""

            while recv_len:
                data= client.recv(4096)
                recv_len = len(data)
                response+= data

                if recv_len<4096:
                    break

            print response,

            #等待更多输入
            buffer = raw_input("")
            buffer += "\n"

            #发送出去
            client.send(buffer)
    except:
        print "[*] Exception! Exiting."

        #关闭链接
        client.close()


