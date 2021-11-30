# RISC-V-Vector and Shader-Hardware Designs in logism
includes a few python scripts to generate logism evolution test vector files for various components
code is commented with description of how the script works
to run a test vector in logism evolution its pretty simple you go to simulate and run the file


# Dependencies
Python 3
Logism Evolution
Java 8 or newer


Python Instructions
1. to make a test file you will need python 3 and ideally some idea (pycharm is probably the easiest) to run it with  but you can do the command line
2. put the text files in the same directory as the python scripts each test file has a corosponding test script
3. now you should have some freshly generated test files

Logism Instructions
1. open logism evolution
2. go to file open and navigate to wererever you got the circ files and open it
3. now that the file is open go to simulate up at the top and click on test vector
4. this should have lead you to a pop up window
5. now load one of the txt files from earlier (which ever one corresponds to the circ you opened if you opened the fpu use the fpu text file)