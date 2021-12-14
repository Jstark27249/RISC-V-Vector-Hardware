# Program to show various ways to read and
# write data in a file.
import math

import numpy as np
import struct

import random


# opcodes
# Bit shift values must go to B Input on the execute
# 000001 or  = shift left
# 000100 = shift right
# 001000 = equivalence check
# 000000 = branching ie < or >
# 000111 or 000101 = subtraction
# 000011 or 000010 = addition
# 000110 = multiplication
# 110000 or 010001 = float multiply
# 110001 = float subtract
# 110000 = float addition



file1 = open("FloatMulTest.txt", "w")
#names must match logism pins (put FloatSubMode[1] where FloatSubMode[0]
floatTestHeader = ["Ain[32]                          ", "Bin[32]                          ", "FPUMulResult[32]                       \n"]
file1.writelines(floatTestHeader)
a = 0.0
b = 0.0
a = np.finfo(np.float32(a)).max
b = np.finfo(np.float32(a)).min
FLOAT_MAX = 3.402823466e+38
FLOAT_MIN = 1.175494351e-38


print(math.sqrt(FLOAT_MAX))
print(math.sqrt(FLOAT_MIN))
randomList = []


print(np.multiply(math.sqrt(FLOAT_MAX), math.sqrt(FLOAT_MIN)))
positive_infinity = float('inf')
negative_infinity = float('-inf')
#convert a floating point number to binary
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', np.float32(num)))


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])



# makes a binary float32 addition problem + its solution



def generateBinaryListAddition(list):
     tempList = []
     overflow = np.float32(1)

     #values constrained to the  sqrt of the float min and max for sake of testing, this should reduce the risk of overflows during testing
     a = np.random.uniform(1.0842021725674597e-19, 1.8446743522909403e+19)
     np.float32(a)

     #overflowing produces garbage when multiplying so the results will always be wrong
     b = np.random.uniform(1.0842021725674597e-19, 1.8446743522909403e+19)
     np.float32(b)

     c = np.multiply(np.float32(a), np.float32(b))
     np.float32(c)
     #print(c)
     a = float_to_hex(a)
     b = float_to_hex(b)


     #sets one as the output if the multiplier overflows
     if c == (positive_infinity or negative_infinity):
          c = overflow
          np.float32(c)
          c = float_to_hex(c)
     else:
          c = float_to_hex(c)





     tempList.append(a)
     tempList.append('      ')
     tempList.append(b)
     tempList.append('      ')
     tempList.append(c)
     tempList.append('      ')
     tempList.append('\n')
     tempList = (map(str, tempList))
     return tempList



#write to the file 32 times with the float addition function
for i in range(0, 32):
    randomList = generateBinaryListAddition(randomList)
    file1.writelines(randomList)




# \n is placed to indicate EOL (End of Line)



file1.close()  # to change file access modes
file1 = open("FloatMulTest.txt", "r+")
