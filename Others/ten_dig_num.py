import itertools
import array
import numpy as np
from collections import Counter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_self_describe_num(input):
    counts = Counter(input)
    valid = True
    for l, digit_value in enumerate(input):
        # The number of times digit 'i' appears should be int(digit_value)
        if counts.get(l, 0) != digit_value:
            valid = False   
    return valid 

def self_describe_num(max_len:int):
    print("Num of Digits:",max_len)
    if(max_len <= 3):
        print("No solution")
    elif(max_len > 3 and max_len <5):
        no_solution = True
        for i in range(10 ** (max_len-1),(10 ** max_len)):
            comb_arr = [int(x) for x in str(i)]
            if is_self_describe_num(comb_arr):
                print("Solution:", i)
                no_solution = False
        if no_solution:
            print("No solution")
            
    elif(max_len > 5 and max_len <= 10):
        for a0 in range(max_len-1,0,-1):

            num_arr = []
            
            for i in range(a0):
                num_arr.append(0)
            
            comb = list(itertools.combinations_with_replacement(numbers, max_len-1 - a0))
            
            for j in comb:
                perm_arr = num_arr.copy()
                for ele in j:
                    perm_arr.append(ele)
                
                if(sum(perm_arr)+a0 == max_len):        
                        

                    comb_k = list(set(itertools.permutations(perm_arr)))
                      
                    for comb in comb_k:
                        comb_arr = array.array('i', comb)
                        if comb_arr[a0-1] >= 1 and comb_arr[0] >= 1:
                            comb_arr.insert(0, a0)

                            
                            if is_self_describe_num(comb_arr):
                                print('Solution:',''.join(str(x) for x in comb_arr))
    else:
        print("Invalid input")

for num in range(1,11):
    self_describe_num(num)