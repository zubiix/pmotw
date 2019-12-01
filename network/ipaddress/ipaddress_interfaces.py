import ipaddress

ADDRESSES = [
    '10.9.0.6/24',
    'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
]

for ip in ADDRESSES:
    interface = ipaddress.ip_interface(ip)
    print('{!r}'.format(interface))
    print('network:\n', interface.network)
    print('ip:\n', interface.ip)
    print('IP with prefixlen:\n',interface.with_prefixlen)
    print('netmask:\n', interface.with_netmask)
    print('hostmask:\n', interface.with_hostmask)
    print()
