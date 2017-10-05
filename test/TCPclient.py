import sys
import socket

if not len(sys.argv[1:]):
	print "usage python tcpclient.py [target_host] [target_port]"
	sys.exit(0)


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

target_host = sys.argv[1]
target_port = sys.argv[2]
#print target_host
#print target_port

client.connect((target_host,int(target_port)))

while True:
	buffer = raw_input("")
        if "x" in buffer:
		break
	buffer += "\n"
        print "[*]Sending %s to %s:%s" %(buffer,target_host,target_port)
	client.send(buffer)
        
        recv_len = 1
	response = ""
	while recv_len:
		data = client.recv(4096)
		recv_len = len(data)
		response += data
		if recv_len < 4096:
			break
	print response,

sys.exit(0)
