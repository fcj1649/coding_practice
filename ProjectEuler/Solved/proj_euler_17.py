import math
from num2words import num2words

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
out = 0
for i in range(1,1001):
    org = i
    word = ''
    dig = int(math.log10(i)) + 1 
    andReq = False
    if(i >= 1000):
        andReq = True
        word += ones[int(i/1000)]+' thousand'

    i = i % 1000

    if(i >= 100):
        andReq = True
        word += ones[int(i/100)]+' hundred'

    i = i % 100

    if(andReq and i != 0):
        word += ' and '

    if( i >=10 and i < 20):
        word += teens[int(i % 10)]
    else:
        if(i >= 20):
            word += tens[int(i/10)]
            i = int(i % 10)
        word += ones[i]
    res = num2words(org).replace('-','').replace(' ', '')
    word = word.replace(' ','')
    out += len(word)
    if(res != word):
        print(org, word, res)

print(out)