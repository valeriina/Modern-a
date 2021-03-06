# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))

# receive data from the server
receive = s.recv(5)
print(receive)
s.send(receive.upper())

# close the connection
s.close()
