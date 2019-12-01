import binascii
import ipaddress

ADDRESSES = [
        '10.9.0.6',
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
]

for ip in ADDRESSES:
    # returns an IPv4Address or IPv6Address
    addr = ipaddress.ip_address(ip)
    print('{!r}'.format(addr))
    print('IP VERSION: ', addr.version)
    print('IS PRIVATE: ', addr.is_private)
    print('PACKED FORM: ', binascii.hexlify(addr.packed))
    print('INTEGER: ', int(addr))
    print()

