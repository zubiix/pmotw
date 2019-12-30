import struct
import binascii

values = (1, 'ab'.encode('utf-8'), 2.7)
print('Original values: ', values)

endianness = [
  ('@', 'native, native'),
  ('=', 'native, standard'),
  ('<', 'little-endian'),
  ('>', 'big-endian'),
  ('!', 'network'),
]

for code, name in endianness:
  s = struct.Struct(code + 'I 2s f')
  packed_data = s.pack(*values)
  print()
  print('Format string: ', s.format, 'for', name)
  print('uses: ', s.size, 'bytes')
  print('Packed value: ', binascii.hexlify(packed_data))
  print('Unpacked value: ', s.unpack(packed_data))

