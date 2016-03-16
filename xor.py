import string
# I'm not cheating, Python's ability to manipulate low level datatypes is poor
from bitstring import BitArray, BitStream 

b1 = '1c0111001f010100061a024b53535009181c'
b2 = '686974207468652062756c6c277320657965'

def xor(s1, s2):
    if len(s1) != len(s2):
        # thrown an error, how do I do that?
        return -99
    # OK, assuming our input is good we can do an XOR
    # if one or other, then one. if both, then 0 - without using Python's XOR operator!
    xor_string = ''
    for i in range(0, len(s1), 2):     # Proceeding one byte at a time
        hex1 = '0x' + s1[i:i+2]
        hex2 = '0x' + s2[i:i+2]
        b1, b2 = BitArray(hex1), BitArray(hex2)
        # print "b1: %s, b2: %s" % (b1, b2),
        res = BitArray('0b00000000')
        # print "hex1: %s, hex2: %s, res: %s" % (hex1, hex2, res), 
        for j in range(0, 8):
            # print j, b1[j:j+1],
            if b1[j:j+1] == '0b1' and b2[j:j+1] == '0b1':
                res[j:j+1] = '0b0'
            else:
                if b1[j:j+1] == '0b1' or b2[j:j+1] == '0b1':
                    res[j:j+1] = '0b1'
        # need to append res to a longer result string
        xor_string += res.hex
    return xor_string

print xor(b1, b2)