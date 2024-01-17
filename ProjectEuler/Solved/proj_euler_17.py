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

def num_to_word(num: int):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    i = num
    result = ''
    if (i >= 10 ** 9):
        result += num_to_word(i // 10 ** 9) + ' Billion'
        i = i % 10 ** 9
    
    if (i >= 10 ** 6):
        result += num_to_word(i // 10 ** 6) + ' Million'
        i = i % 10 ** 6
    
    if (i >= 10 ** 3):
        result += num_to_word(i // 10 ** 3) + ' Thousand'
        i = i % 10 ** 3
        
    if (i >= 10 ** 2):
        result += ones[(i // 10 ** 2)] + ' Hundred'
        i = i % 10 ** 2
    
    if (i >=10 and i < 20):
        result += teens[int(i % 10)]
    else:
        if (i >= 20):
            result += tens[i // 10]
            i = int(i % 10)
        result += ' ' + ones[i]
    return result

for i in range(10**6, 10**7):
    a = num2words(i).replace('-','').replace(' and','').replace(' ','').replace(',','').lower()
    b = num_to_word(i).replace(' ','').lower()
    if(a != b):
        print(i, a, b)