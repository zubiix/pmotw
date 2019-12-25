import decimal

# set up a context with limited preicision
c = decimal.getcontext().copy()
c.prec = 3

# create our constant
pi = c.create_decimal('3.1415')

# the constant value is rounded off
print('PI : ', pi)

# the result of using the constant uses the global context precision
print('RESULT: ', decimal.Decimal('2.01') * pi)
