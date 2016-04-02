import sys
import os

def  prevSmaller(arr):
    output = [-1]
    stack = []
    stack.append(arr[0])
        
    for index in range(1, len(arr)):
        while len(stack) and arr[index] <= stack[-1]:
            stack.pop()
                
        if not len(stack):
            output.append(-1)
        else:
            output.append(stack[-1])
        stack.append(arr[index])
        
    return output

f = open('output05.txt', 'w')
    

_arr_cnt = 0
_arr_cnt = int(raw_input())
_arr_i=0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = int(raw_input());
    _arr.append(_arr_item)
    _arr_i+=1
    

res = prevSmaller(_arr);
for res_cur in res:
    f.write(str(res_cur) + "\n")

f.close()

