import string
# I'm not cheating, Python's ability to manipulate low level datatypes is poor
from bitstring import BitArray, BitStream 

chars = string.ascii_uppercase + string.ascii_lowercase + "0123456789+/"
base64_index = zip(range(0,64), chars)

# Grab hex string for message to be encoded
msg = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# Represent msg as binary
# Starting from left
#   Group message into 3 byte (24 bit) sequences
#   Calculate int value of every group of 6 bits - yielding 4 characters
#   Lookup character value for that int in ASCII table

r = len(msg) % 6 
if r != 0:
    msg.append(r*'00')              # pad msg to be a mult of 3 bytes

encoded_msg = ''
for i in range(0, len(msg), 6):     # Collect 3 bytes at a time (6 half-words)
    hex = '0x' + msg[i:i+6]         # set up a hex string for these 3 bytes
    bseq = BitArray(hex)            # convert to a binary bitstring
    for j in range(0, 24, 6):       # group every 6 bits
        val = bseq[j:j+6].int       # convert to an int for lookup
        encoded_msg += chars[val]    # and lookup the appropriate character

# While this works, it is technically incomplete. If the final bytes require padding to complete a 
# grouping of three, those are to be translated as "=" or "==". It's complicated.

print encoded_msg