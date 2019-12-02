#!/usr/bin/python
import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the soket to the port
server_address = ('127.0.0.1', 10000)
print('Starting server on {} port:{}'.format(*server_address))
sock.bind(server_address)

# listen for incoming connections
sock.listen(1)

while True:
  # wait for a connection
  print('Waiting for connection')
  connection, client_address = sock.accept()
  try:
    print('New Connection from', client_address)
    
    # recieve the trasmitted data in small chunks and retransmit
    while True:
      data = connection.recv(1024)
      print('recieved {!r}'.format(data))
      if data:
        print('Transmitting data back to client')
        connection.sendall(data)
      else:
        print('No data from', client_address)
        break
  finally:
    connection.close()
