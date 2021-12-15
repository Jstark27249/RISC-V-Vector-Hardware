# RISC-V-Vector and Shader-Hardware Designs in logism

# Goal
Goal of this project was to build some basic RISC-V compliant vector hardware. I have decided to put it all on github cause learning about this topic was miserable as its all scattered through research papers and obscure power points. So I want to make this work easy for anyone interest to play around with it. This repository contains the backend of RISC-V compliant rudimentary shader core/vector processor. It also contains some basic test scripts to automate testing via logism-evolutions test vector feature. The Shader execute backend I then packed into a full simd execute capable of operating on a 128 bit vector to pair with a large register file to complete the full basic shader core. Hopefully someone can find a use for this for their own projects or learning purposes.

# Includes
1. Test scripts in python along with txt files that correspond to said script
2. All Circuit Files Used
3. Photos of circuits with comments

# Dependencies 
Python 3
https://www.python.org/downloads/
-----------------
Logism Evolution
https://github.com/logisim-evolution/logisim-evolution
-----------------
Java 8 or newer
https://adoptium.net/
-----------------

# Python Instructions
0. You will need the python libraries numpy, struct, and random. If you open the scripts in pycharm it will make things much easier to work with and should install the packages for you.
1. to make a test file you will need python 3 and ideally some idea (pycharm is probably the easiest) to run it with  but you can do the command line
2. put the text files in the same directory as the python scripts each test file has a corosponding test script
3. now you should have some freshly generated test files.
4. To modify the test to make different ones edit the scripts, they are commented to make it easier. 
-----
5. The floating point scripts work specifically for the floating point designs execution units which are listed under the FPUMul.FPUmul and FPUAdder32.FPUAdder
6. The Int scripts work on the enhanced ALU circuit 32bit alu subcircuit but can also work on the SimdShaderExecute backend subcircuit if you modify the header opcode to match it (chang it from a 4 to a 6 bit opcode)

# Logism Instructions
0. The full shader is a macro unit of all the other circ files so you would need to load those files as a logism library first to be able to use it. Here is a video on how to load a library in logism classic (the rules are same for evolution except you choose logism-evolution library) https://www.youtube.com/watch?v=0XtfIvPP-P0 
1. open logism evolution
2. go to file open and navigate to wererever you got the circ files and open it
3. now that the file is open go to simulate up at the top and click on test vector
4. this should have lead you to a pop up window
5. now load one of the txt files from earlier, they should all run on the sub circuit labeled ShaderExecutBackend in the VectorSimdShader File
6. It is important to note with regards to the floating point testing the results have a range of about +/-1 bit as a result of the imprecise nature of floating point arithmetic. You should expect to see a false negative about 50% as a result of the imperfect of lossy conversion to binary and the  impresise nature of floating point mathematics as a result of the rounding involved. So when you run a floating point script expect about 50% failure rate but said failed outputs should only ever be about +/- 1 bit from the expected. When you run a test vector in logism you can mouse or the result to see the level of error. If its within that range it means its a false negative and its working as intended.
7. IF your still confused on how to run a test vector here is a video on not just how to run one but how to make one aswell. https://www.youtube.com/watch?v=GdDnEPFlXbI
8. Alternatively you can skip the test vector stuff and just play around with the design manually.


