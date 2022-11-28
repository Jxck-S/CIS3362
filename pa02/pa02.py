# /*=============================================================================
# | Assignment: pa02 - Calculating an 8, 16, or 32 bit
# | checksum on an ASCII input file
# |
# | Author: Jack Sweeney
# | Language: Python
# |
# | To Compile: javac pa02.java
# | gcc -o pa02 pa02.c
# | g++ -o pa02 pa02.cpp
# | go build pa02.go
# | python pa02.py //Caution - expecting input parameters
# |
# | To Execute: java -> java pa02 inputFile.txt 8
# | or c++ -> ./pa02 inputFile.txt 8
# | or c -> ./pa02 inputFile.txt 8
# | or go -> ./pa02 inputFile.txt 8
# | or python-> python pa02.py inputFile.txt 8
# | where inputFile.txt is an ASCII input file
# | and the number 8 could also be 16 or 32
# | which are the valid checksum sizes, all
# | other values are rejected with an error message
# | and program termination
# |
# | Note: All input files are simple 8 bit ASCII input
# |
# | Class: CIS3360 - Security in Computing - Fall 2022
# | Instructor: McAlpin
# | Due Date: per assignment
# |
# +=============================================================================*/
import sys

def print_80(stringy):
    line_length = 80+1
    for i in range(0,len(stringy),line_length):
        print(stringy[i:i+line_length])
def calc_pad(str_in, bits):
    pad = 0
    str_len = len(str_in)
    mod = 4 if bits == 32 else 2
    while (str_len % mod != 0):
        str_len += 1
        pad += 1
    return pad if bits > 8 else 0
def add_pad(str_in, pad_count):
    if pad_count > 0:
        for x in range(0, pad_count):
            str_in += "X"
    return str_in

def checksum(text, bits):
    checksum = 0
    if bits == 8:
        for c in text:
            checksum += ord(c)
        cs = ("%x" % checksum).strip("")[-2:].strip("0")
        return cs
    elif bits == 16:
        for i in range(0, len(text)-1, 2):
            checksum += ((ord(text[i]) << 8) | (ord(text[i + 1])))
        cs = ("%x" % checksum).strip("")[-4:].strip("0")
        return cs
    else:
        for i in range(0, len(text)-1, 4):
            checksum += ((ord(text[i]) << 24) | (ord(text[i + 1]) << 16) | (ord(text[i + 2]) << 8) | (ord(text[i + 3])))
        cs = ("%x" % checksum).strip("")[-8:]
        return cs

if len(sys.argv) < 3:
    raise ValueError("Bad args provided.")
input_file_name = sys.argv[1]
bits = int(sys.argv[2])
if bits not in [8, 16, 32]:
    sys.stderr.write("Valid checksum sizes are 8, 16, or 32\n")
    exit()

input_file = open(input_file_name, "r",encoding="utf8")
input_text = input_file.read()
padding = calc_pad(input_text, bits)
padded_text = add_pad(input_text, padding)
pad_str_len = len(padded_text)
cs = checksum(padded_text, bits)
print_80("\n"+padded_text)
print_80("%2d bit checksum is %8ls for all %4d chars" % (bits, cs, pad_str_len))

# /*=============================================================================
# | I Jack Sweeney (ja815158) affirm that this program is
# | entirely my own work and that I have neither developed my code together with
# | any another person, nor copied any code from any other person, nor permitted
# | my code to be copied or otherwise used by any other person, nor have I
# | copied, modified, or otherwise used programs created by others. I acknowledge
# | that any violation of the above terms will be treated as academic dishonesty.
# +=============================================================================*/