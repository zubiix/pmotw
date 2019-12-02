import socket

def get_constants(prefix):
    return {
            getattr(socket,n):n
            for n in dir(socket)
            if n.startswith(prefix)
    }

families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

responses = socket.getaddrinfo(
    host='www.python.org',
    port='http',
    family=socket.AF_INET,
    type=socket.SOCK_STREAM,
    proto=socket.IPPROTO_TCP,
    flags=socket.AI_CANONNAME,  
)

for response in responses:
    family, socktype, proto, canonname, sockaddr = response
    print('family:', families[family])
    print('type:', types[socktype])
    print('protocol:', protocols[proto])
    print('canonical name:', canonname)
    print('socket address:', sockaddr)
    print()



