import sys
import os


def  singleNumber(A):
    x = 1
    output = 0
        
    for i in range(32):
        # Get Individual bits
        count_0 = 0
        count_1 = 0
            
        for num in A:
            if num & x:
                count_1 += 1
            else:
                count_0 += 1
            
            
        # print count_1
        if count_1 % 3 == 1:
            output +=  pow(2, i)
        x = x << 1
        
    return output

f = open('output04.txt', 'w')
    

_A_cnt = 0
_A_cnt = int(raw_input())
_A_i=0
_A = []
while _A_i < _A_cnt:
    _A_item = int(raw_input());
    _A.append(_A_item)
    _A_i+=1
    

res = singleNumber(_A);
f.write(str(res) + "\n")

f.close()


