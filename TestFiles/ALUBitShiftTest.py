# Program to show various ways to read and
# write data in a file.

import struct
import random
import numpy as np

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

file1 = open("ALUBitShiftTest.txt", "w")
# names must match logism pins (put FloatSubMode[1] where FloatSubMode[0]
floatTestHeader = ["A[32]                                 ", "B[32]                                 ",
                   "Result[32]                            ", "Opcode[4]  ", "shiftAmount[5]   ", "ErrorBit[1]\n"]
file1.writelines(floatTestHeader)

randomList = []


# convert a int point number to binary, did hex here cause python was being dumb with binary
def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))


def bitShiftLeft (val, shift):
    val = np.int32(val) << np.int32(shift)
    return val

def bitShiftRight (val, shift):
    val = np.int32(val) >> np.int32(shift)
    return val


# this test also works for right shifting aswell just swap the bit shift function to the right function and swap the opcode accordingly
# makes a binary int32 addition problem + its solution
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


# 0000 = bit shift b input left by shift input amount (currently I do not have a auto generator for this operation at the moment but you can play around with it anyway in the circ file if you want)
# bit shifting is probably the least interesting thing its literally shift left or right by 0-32 bits
# well either that or branching

def generateBinaryListAddition(list):
    tempList = []
    a = random.randint(-2147483648, 2147483647)
    b = random.randint(-2147483648, 2147483647)
    e = random.randint(0, 31) # shift amount change it between binary value of 0 and 32 so 11111 = 32
    d = "000001       "  # opcode


    c = bitShiftLeft(b, e)
    e = tohex(e, 5)  # shift input takes 5 number
    f = "0      "  # default 0 output/errorbit should be zero unless it overflows or underflows which happesn if it exceeds integer min or max for 32 bit unsigned int

    if (c > 2147483647 or c < -2147483648):
        f = "1      "
    else:
        f = "0      "  # zero output, should always be 0 unless value exceeds sign integer max or min

    a = tohex(a, 32)
    b = tohex(b, 32)
    c = tohex(c, 32)
    tempList.append(a)
    tempList.append('      ')
    tempList.append(b)
    tempList.append('      ')
    tempList.append(c)
    tempList.append('      ')
    tempList.append(d)
    tempList.append(e)
    tempList.append('      ')
    tempList.append(f)
    tempList.append('\n')
    tempList = (map(str, tempList))
    return tempList


# write to the file 32 times with the float addition function
for i in range(0, 32):
    randomList = generateBinaryListAddition(randomList)
    file1.writelines(randomList)

# \n is placed to indicate EOL (End of Line)


file1.close()  # to change file access modes
file1 = open("ALUBitShiftTest.txt", "r+")
print(100 << 10)