import binascii 
import socket
import struct
import sys

for string_address in ['192.168.1.1', '127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print('orginal:', string_address)
    print('packed:', binascii.hexlify(packed))
    print('unpacked:', socket.inet_ntoa(packed))
    print()
