import threading
import socket
import sys
def main():
    if not len(sys.argv[1:]):
        print "server"
        server()
    else:
        client()
    return

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "%s" % request

    client_socket.send("ACK!")
    client_socket.close()

def server():
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(("0.0.0.0",9999))
    server.listen(5)
    while True:
        client,addr = server.accept()

        print "connection from %s:%d"%(addr[0],addr[1])

        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

def client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("127.0.0.1",9999))
    client.send("123123123")
    response = client.recv(4096)
    print response

main()
