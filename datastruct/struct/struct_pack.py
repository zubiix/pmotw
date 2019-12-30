import struct
import binascii

# use struct pack to convert a string to a packed byte
values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)

print('Original values: ', values)
print('Format String: ', s.format)
print('Uses: ', s.size, 'bytes')
print('Packed Value: ', binascii.hexlify(packed_data))