import math
str = ''
file = open('.\ProjectEuler\Solved\proj_euler_42_words.txt', 'r')
words = file.readlines()[0].strip().replace('"','').split(',')
count = 0
for word in words:
    sum_word = sum((ord(x) - ord('A') + 1) for x in list(word))
    # get roots of n^2 + n - 2 * sum_word
    b = 1
    a = 1
    c = -2 * sum_word
    root_1 = (-b + math.sqrt(b * b - 4 * a * c)) / ( 2 * a )
    if(root_1.is_integer() and root_1 > 0):
        count +=1 
        print(word, sum_word, root_1)
    else:
        root_2 = (-b - math.sqrt(b * b - 4 * a * c)) / ( 2 * a )
        if(root_2.is_integer() and root_2 > 0):
            count +=1 
            print(word, sum_word, root_2)            
print(count)