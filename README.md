# RISC-V-Vector and Shader-Hardware Designs in logism
includes a few python scripts to generate logism evolution test vector files for various components
code is commented with description of how the script works
to run a test vector in logism evolution its pretty simple you go to simulate and run the file


# Dependencies
Python 3
------
Logism Evolution
------
Java 8 or newer
------

Python Instructions
0. You will need the python libraries numpy, struct, and random. If you open the scripts in pycharm it will make things much easier to work with and should install the packages for you.
1. to make a test file you will need python 3 and ideally some idea (pycharm is probably the easiest) to run it with  but you can do the command line
2. put the text files in the same directory as the python scripts each test file has a corosponding test script
3. now you should have some freshly generated test files.
4. To modify the test to make different ones edit the scripts, they are commented to make it easier. 


Logism Instructions
1. open logism evolution
2. go to file open and navigate to wererever you got the circ files and open it
3. now that the file is open go to simulate up at the top and click on test vector
4. this should have lead you to a pop up window
5. now load one of the txt files from earlier, they should all run on the sub circuit labeled ShaderExecutBackend in the VectorSimdShader File
6. It is important to note with regards to the floating point testing the results have a range of about +/-1 bit as a result of the imprecise nature of floating point arithmetic. You should expect to see a false negative about 50% as a result of the imperfect of lossy conversion to binary and the  impresise nature of floating point mathematics. So when you run a floating point script expect about 50% failure rate but said failed outputs should only ever be about +/- 1 bit from the expected. When you run a test vector in logism you can mouse or the result to see the level of error. If its within that range it means its a false negative and its working as intended.
7. IF your still confused on how to run a test vector here is a video on not just how to run one but how to make one aswell. https://www.youtube.com/watch?v=GdDnEPFlXbI

