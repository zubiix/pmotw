import decimal

d = decimal.Decimal('0.123456')

# change precision for the values of d
for i in range(1, 5):
  decimal.getcontext().prec = i
  print(i, ':', d, d * 1)
