# A networks is defined by a range of addresses. 
# it is usually expressed with a base address and a mask
# indicating which portion of the address represents the network

import ipaddress

NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
]

for n in NETWORKS:
    net = ipaddress.ip_network(n)
    print('{!r}'.format(net))
    print('is private:', net.is_private)
    print('broadcast:', net.broadcast_address)
    print('compressed:', net.compressed)
    print('with netmask:', net.with_netmask)
    print('with hostmask:', net.with_hostmask)
    print('num addresses:', net.num_addresses)
    print()
