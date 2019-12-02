import socket

hostname, aliases, addresses = socket.gethostbyaddr('151.101.16.223')

print('hostname:', hostname)
print('aliases:', aliases)
print('addresses:',addresses)

