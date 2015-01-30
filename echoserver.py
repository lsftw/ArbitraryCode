# Started from http://ilab.cs.byu.edu/python/socket/echoserver.html
import socket

def hostOn(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    return s

def main():
    host = ''
    port = 50000
    s = hostOn(host, port)
    backlog = 5
    size = 1024
    s.listen(backlog)
    while 1:
        client, address = s.accept()
        data = client.recv(size)
        if data:
            print(data)
            client.send(data)
        client.close()

if __name__ == '__main__':
    main()
