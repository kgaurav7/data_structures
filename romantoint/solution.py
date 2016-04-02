import os
import sys

# Complete the function below.


def  romanToInt(A):
    roman_num = {"IV" : 4, "IX" : 9, 
                 "XL": 40, "XC": 90, 
                 "CD" : 400, "CM": 900, 
                 "I": 1, "V": 5, "X": 10, "L" : 50, "C" : 100,
                 "D" : 500, "M": 1000}
        
        
    check_required = ["I", "X", "C"] 
    output = 0
    skip = False
        
    for index in range(len(A)):
        if skip:
            skip = False
            continue
            
        if A[index] not in check_required or index == (len(A)-1):
            output += roman_num[A[index]]
            
        else:
            if A[index] == "I":
                if A[index + 1] == "V":
                    output += roman_num["IV"]
                    skip = True
                elif A[index + 1] == "X":
                    output += roman_num["IX"]
                    skip = True
                else:
                    output += roman_num[A[index]]
                        
            elif A[index] == "X":
                if A[index + 1] == "L":
                    output += roman_num["XL"]
                    skip = True
                elif A[index + 1] == "C":
                    output += roman_num["XC"]
                    skip = True
                else:
                    output += roman_num[A[index]]
                
            elif A[index] == "C":
                if A[index + 1] == "D":
                    output += roman_num["CD"]
                    skip = True
                elif A[index + 1] == "M":
                    output += roman_num["CM"]
                    skip = True
                else:
                    output += roman_num[A[index]]
    return output


f = open(os.environ['OUTPUT_PATH'], 'w')
    

_A = raw_input()

res = romanToInt(_A);
f.write(str(res) + "\n")

f.close()
