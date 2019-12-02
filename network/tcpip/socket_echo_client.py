#!/usr/local/bin/python3
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {}:{}'.format(*server_address))
sock.connect(server_address)

try:
  # send data
  message = b'this is the message. it will be repeated'
  print('sending {!r}'.format(message))
  sock.sendall(message)

  # look for response
  amount_received = 0
  amount_expected = len(message)

  while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print('received {!r}'.format(data))

finally:
  print('closing bracket')
  sock.close()
