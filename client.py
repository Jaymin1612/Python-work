import socket

def Main():
    host = input("Enter the host name: ")
    port = input("Enter the port number: ")

    s = socket.socket()
    s.connect((host, port))

    message = input("-> ")
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024)
        print ('Received from server: ',str(data))
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()