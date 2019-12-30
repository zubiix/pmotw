import struct
import binascii

# get the packed data
packed_data = binascii.unhexlify(b'0100000061620000cdcc2c40')

s = struct.Struct('I 2s f')

# unpack the sequence of hex bytes
unpacked_data = s.unpack(packed_data)
print('Unpacked values: ', unpacked_data)
