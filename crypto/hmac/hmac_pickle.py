import hashlib
import hmac
import io
import pickle
import pprint

def make_digest(message):
    "Return a digest for the message"
    hash = hmac.new(
            b'secret-shared-key-goes-here',
            message,
            hashlib.sha1,
    )
    return hash.hexdigest().encode('utf-8')

class SimpleObject:
    '''
    Demonstrates checking digests before printing
    '''
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

# simulate a writable socket or pipe with a buffer
out_s = io.BytesIO()

# write a valid object to the stream:
# digest\nlength\npickle

o = SimpleObject('digeset matches')
pickled_data = pickle.dumps(o)
digest = make_digest(pickled_data)
header = b'%s %d\n' % (digest, len(pickled_data))
print('Writing: {}'.format(header))
out_s.write(header)
out_s.write(pickled_data)

# write an invalid object to the stream
o = SimpleObject('digest does not match')
pickled_data = pickle.dumps(o)
digest = make_digest(b'not the pickled data at all')
header = b'%s %d \n' % (digest, len(pickled_data))
print('\n Writing: {}'.format(header))
out_s.write(header)
out_s.write(pickled_data)

out_s.flush()

# simulate a readalbe socket or pipe with a buffer
in_s = io.BytesIO(out_s.getvalue())

# read the data
while True:
    first_line = in_s.readline()
    if not first_line:
        break
    incoming_digest, incoming_length = first_line.split(b' ')
    incoming_length = int(incoming_length.decode('utf-8'))
    print('\n Read:', incoming_digest, incoming_length)

    incoming_pickled_data = in_s.read(incoming_length)
    actual_digest = make_digest(incoming_pickled_data)
    print('Actual:', actual_digest)

    if hmac.compare_digest(actual_digest, incoming_digest):
        obj = pickle.loads(incoming_pickled_data)
        print('OK:', obj)
    else:
        print('Warning: Data corruption')
