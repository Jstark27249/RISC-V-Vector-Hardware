# Program to show various ways to read and
# write data in a file.

import struct
import random

file1 = open("ALUIntTest.txt", "w")
# names must match logism pins (put FloatSubMode[1] where FloatSubMode[0]
floatTestHeader = ["A[32]                                 ", "B[32]                                 ",
                   "Result[32]                            ", "Opcode[4]  ", "shiftAmount[5]   ", "ErrorBit[1]\n"]
file1.writelines(floatTestHeader)

randomList = []


# convert a int point number to binary, did hex here cause python was being dumb with binary
def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))


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

def generateBinaryListAddition(list):
    tempList = []
    a = random.randint(-2147483648, 2147483647)
    b = random.randint(-2147483648, 2147483647)

    d = "00011       "  # opcode
    e = "00000      "  # shift amount change it between binary value of 0 and 32 so 11111 = 32
    f = "0      "  # default 0 output/errorbit should be zero unless it overflows or underflows which happesn if it exceeds integer min or max for 32 bit unsigned int
    c = a + b;
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
file1 = open("intTest.txt", "r+")
