# Program to show various ways to read and
# write data in a file.

import struct

file1 = open("floatTest.txt", "w")
#names must match logism pins (put FloatSubMode[1] where FloatSubMode[0]
floatTestHeader = ["Float32A[32]                          ", "Float32B[32]                          ", "FloatResult[32]                       ",  "FloatSubMode[1]\n"]
file1.writelines(floatTestHeader)


import random
randomList = []


#convert a floating point number to binary
def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

# makes a binary float32 addition problem + its solution
def generateBinaryListAddition(list):
     tempList = []
     a = random.uniform(-2 ^ 32, 2 ^ 31)
     b = random.uniform(-2 ^ 32, 2 ^ 31)
     c = a + b;
     d = 0 #mode for floatsubmode pin
     a = binary(a)
     b = binary(b)
     c = binary(c)
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
file1 = open("floatTest.TXT", "r+")
