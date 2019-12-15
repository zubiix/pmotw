# read and write contents of an array to and from file
import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1:', a)

# write the array of numbers to a temporary file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)
output.flush()

# read the raw data
with open(output.name, 'rb') as input:
    raw_data = input.read()
    # read the file content and print the hex
    print('raw contents: ', binascii.hexlify(raw_data))

    # read the data into an array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)
    

