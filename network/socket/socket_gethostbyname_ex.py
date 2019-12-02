import socket

HOSTS = [
        'apu',
        'pymotw.com',
        'www.python.org',
        'nosuchname',
]

for host in HOSTS:
    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)
        print('Hostname:',name)
        print('Aliases:',aliases)
        print('Addresses:',addresses)
    except socket.error as msg:
        print('Error:', msg)
    print()
