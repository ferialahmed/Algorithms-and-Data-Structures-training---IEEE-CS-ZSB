import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    s = n.strip()
    size = len(s)
    sum = int(s[0])
    total = sum
    for i in range (1, size):
        total= (total*10+int(s[i])*(i+1))%(10**9+7)
        sum = (total+sum)%(10**9+7)
    return(sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
