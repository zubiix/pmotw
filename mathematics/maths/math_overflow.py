x = 10.0 ** 200

print('x = ', x)
print('x * x =', x * x)
print('x ** 2 =', end='')
try:
  print(x ** 2)
except OverflowError as e:
  print(e)