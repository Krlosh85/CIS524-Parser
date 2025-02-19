'''
Authors: Carlos Herrera
CIS 524 - Comparative Programming Languages
Instructor: Aditi Singh, PhD

Coding assignment - Top Down Recursive-descent parser using python
'''

import sys

# Classes and token codes taken from the parcer.c provided on BB
#Character classes
LETTER = 0
DIGIT = 1
UNKNOWN = 99

#Token codes
INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
SEMI_COLON = 27
PRINT = 28

# WIP

if __name__ == "__main__":
    # Checking for correct usage of the code
    if len(sys.argv) < 2:
        print("To use this parser use the following form: parser_2814075.py input_file")
        sys.exit(1)
    
    
    
    