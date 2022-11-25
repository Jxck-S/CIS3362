# /*=============================================================================
# | Assignment: pa01 - Encrypting a plaintext file using the Vigenere cipher
# |
# | Author: Jack Sweeney
# | Language: python
# |
# | To Compile: javac pa01.java
# | gcc -o pa01 pa01.c
# | g++ -o pa01 pa01.cpp
# | go build pa01.go
# | python pa01.py
# |
# | To Execute: java -> java pa01 kX.txt pX.txt
# | or c++ -> ./pa01 kX.txt pX.txt
# | or c -> ./pa01 kX.txt pX.txt
# | or go -> ./pa01 kX.txt pX.txt
# | or python -> python pa01.py kX.txt pX.txt
# | where kX.txt is the keytext file
# | and pX.txt is plaintext file
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
    line_length = 80
    for i in range(0,len(stringy),line_length):
        print(stringy[i:i+line_length])

if len(sys.argv) == 1:
    raise ValueError("No file names provided.")
encrypt_key_file = sys.argv[1]
plain_text_file = sys.argv[2]
#print(f"Key {encrypt_key_file}, text {plain_text_file}")

encrypt_key_file = open(encrypt_key_file, "r",encoding="utf8")
encrypt_key = encrypt_key_file.read().lower()
new_encrypt_key = ""
for char in encrypt_key:
    if char.isalpha():
        new_encrypt_key += char

plain_text_file = open(plain_text_file, "r",encoding="utf8")
plain_text = plain_text_file.read().lower()
new_plain_text = ""
for char in plain_text:
    if char.isalpha():
        new_plain_text += char
#EXPAND TEXT
while len(new_plain_text) < 512:
    new_plain_text += "x"
new_plain_text = new_plain_text[0:512]
new_copy = new_encrypt_key
#EXPAND KEY
print("\n\nVigenere Key:\n")
print_80(new_encrypt_key)
while len(new_copy) != len(new_plain_text):
    new_copy += new_encrypt_key[0:(len(new_plain_text)-len(new_copy))]
new_encrypt_key = new_copy
print("\n\nPlaintext: \n")
print_80(new_plain_text)

alpha = "abcdefghijklmnopqrstuvwxyz"
cip_txt =""
for i in range(0, len(new_plain_text)):
    char = new_plain_text[i]
    key_idx = i % len(new_encrypt_key)
    key_char = new_encrypt_key[key_idx]
    key_code = alpha.index(key_char)
    char_num = alpha.index(char)

    char_code = (key_code + char_num) % len(alpha)
    cip_char = alpha[char_code]
    cip_txt += cip_char

print("\n\nCiphertext:\n")
print_80(cip_txt)

# /*=============================================================================
# | I Jack Sweeney (ja815158) affirm that this program is
# | entirely my own work and that I have neither developed my code together with
# | any another person, nor copied any code from any other person, nor permitted
# | my code to be copied or otherwise used by any other person, nor have I
# | copied, modified, or otherwise used programs created by others. I acknowledge
# | that any violation of the above terms will be treated as academic dishonesty.
# +=============================================================================*/