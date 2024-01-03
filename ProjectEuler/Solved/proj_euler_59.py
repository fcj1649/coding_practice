import math
import pathlib, os
import re
path = os.path.join(pathlib.Path(__file__).parent.resolve(),'proj_euler_0059_cipher.txt')

file = open(path, 'r')
input = []
for line in file.readlines():
    input.extend([int(x) for x in line.strip().split(',')])

for i in range(26):
    for j in range(26):
        for k in range(26):
            key = [i+97, j+97, k+97]
            words = ''
            out = 0
            isValid = True
            for l in range(len(input)):
                xor_val = input[l] ^ key[l % 3]
                ascii_chr = chr(xor_val)
                if((ascii_chr >= '0' and ascii_chr <= '9') or
                   (ascii_chr >= 'A' and ascii_chr <= 'Z') or
                   (ascii_chr >= 'a' and ascii_chr <= 'z') or
                   (ascii_chr == ' ') or
                   (ascii_chr == ',') or
                   (ascii_chr == '.') or
                   (ascii_chr == '?') or
                   (ascii_chr == '!') or
                   (ascii_chr == ';') or
                   (ascii_chr == '-') or
                   (ascii_chr == ')') or
                   (ascii_chr == '(') or
                   (ascii_chr == ']') or
                   (ascii_chr == '[') or
                   (ascii_chr == "'") or 
                   (ascii_chr == '"') or
                   (ascii_chr == ':') or 
                   (ascii_chr == '+') or
                   (ascii_chr == '\\')or 
                   (ascii_chr == '/')): 
                    words+= ascii_chr
                    out+=xor_val
                else:
                    isValid = False
                    break
                        
                        
            if( isValid ):
                print(words, ''.join(chr(x) for x in key), out)
                break
