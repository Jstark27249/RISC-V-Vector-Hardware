# Program to show various ways to read and
# write data in a file.
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


file1 = open("FloatAddTest.txt", "w")
#names must match logism pins (put FloatSubMode[1] where FloatSubMode[0]
floatTestHeader = ["Float32A[32]                          ", "Float32B[32]                          ", "FloatResult[32]                       ",  "FloatSubMode[1]\n"]
file1.writelines(floatTestHeader)


FLOAT_MAX =np.float32(1 * (2-2^(-23)) * 2^127)
FLOAT_MIN =np.float32(1 * (2-2^(-23)) * 2^-126)
randomList = []


#this test also works for floating point subtraction but you need to swap the addition in line 41 to to subtraction and change the opcode
#convert a floating point number to binary
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', np.float32(num)))


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])



# makes a binary float32 addition or subtraction problem + its solution



def generateBinaryListAddition(list):
     tempList = []

     a = np.random.uniform(FLOAT_MIN, FLOAT_MAX)
     np.float32(a)
     b = np.random.uniform(FLOAT_MIN, FLOAT_MAX)
     np.float32(b)


     c = np.add(a, b)
     np.float32(c)
     d = 0 # mode pin
     a = float_to_hex(a)
     b = float_to_hex(b)
     c = float_to_hex(c)

     tempList.append(a)
     tempList.append('      ')
     tempList.append(b)
     tempList.append('      ')
     tempList.append(c)
     tempList.append('      ')
     tempList.append(d)
     tempList.append('\n')
     tempList = (map(str, tempList))
     return tempList



#write to the file 32 times with the float addition function
for i in range(0, 32):
    randomList = generateBinaryListAddition(randomList)
    file1.writelines(randomList)




# \n is placed to indicate EOL (End of Line)



file1.close()  # to change file access modes
file1 = open("FloatAddTest.txt", "r+")
