# Author: Unisse Chua, NYU, September 2017

from __future__ import print_function
import sys

if not len(sys.argv) == 2:
    print("Invalid number of arguments. Run as python aSimplePythonScript.py YourNameHere")
    sys.exit()

# this line prints Hallo and then your name
# which you provide as an argument
print("Hallo " + sys.argv[1] + "!")
