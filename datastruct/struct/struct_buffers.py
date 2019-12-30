import struct
import binascii
import ctypes
import array

s = struct.Struct('I 2s f')
values = (1, 'ab'.encode('utf-8'), 2.7)
print('Original: ', values)

print()
print('ctype string buffer')

b = ctypes.create_string_buffer(s.size)
print('Before: ', binascii.hexlify(b.raw))

# instead of creating  new instance we can avoid the overhead
# of allocating a new buffer
s.pack_into(b, 0, *values)
print('After: ', binascii.hexlify(b.raw))
print('Unpacked: ', s.unpack_from(b, 0))

print()
print('array')

# create an array of bytes with the size of the string
a = array.array('b', b'\0' * s.size)
print('Before: ', binascii.hexlify(a))
s.pack_into(a, 0, *values)
print('After: ', binascii.hexlify(a))
print('Unpacked: ', s.unpack_from(a, 0))

