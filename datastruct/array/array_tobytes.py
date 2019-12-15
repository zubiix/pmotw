import array
import binascii

a = array.array('i', range(5))
print('A1: ', a)

# convert array elements to bytes
as_bytes = a.tobytes()
print('bytes:', binascii.hexlify(as_bytes))

a2 = array.array('i')
a2.frombytes(as_bytes)
print('A2:', a2)
