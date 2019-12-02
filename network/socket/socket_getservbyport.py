# this reverse lookup is useful for constructing url
# to services from arbitrary addresses

import socket
from urllib.parse import urlunparse

for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    url = '{}://example.com/'.format(socket.getservbyport(port))
    print(url)

