# Started from http://ilab.cs.byu.edu/python/socket/echoclient.html
# and http://ilab.cs.byu.edu/python/socket/echoserver.html
import socket

def connectTo(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	return s

def getPublicIp():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('google.com', 0)) # dummy socket to get ip, sorry google
	return s.getsockname()[0]

def main():
	print('Your IP: ', getPublicIp())
	# host = '129.2.209.207'
	# port = 50000
	# s = connectTo(host, port)
	# send messages
	# message = raw_input(">")
	# size = 1024
	# s.send(message)
	# data = s.recv(size)
	# print data
	# s.close()

if __name__ == "__main__":
	main()
