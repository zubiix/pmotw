import array
import pprint

a = array.array('i', range(3))
print('Initial :', a);

a.extend(range(3))
print('extended:', a)

print('slice: ', a[2:5])
print('Iterator:', list(enumerate(a)))
