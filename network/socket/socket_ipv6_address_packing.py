import binascii 
import socket
import struct
import sys

string_address = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
packed = socket.inet_pton(socket.AF_INET6, string_address)
print('orginal:', string_address)
print('packed:', binascii.hexlify(packed))
print('unpacked:', socket.inet_ntop(socket.AF_INET6,packed))
print()
