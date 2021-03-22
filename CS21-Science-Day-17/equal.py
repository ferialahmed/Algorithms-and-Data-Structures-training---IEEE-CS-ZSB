import math
import os
import random
import re
import sys

# Complete the equal function below.

target=[0,1,2]
def equal(arr):
    min_arr = min(arr)
    results = [0] * len(target)
    for item in arr:
        for i in target:
            gap = item - min_arr + i
            results[i] += gap // 5 + (gap%5) // 2 + (gap%5)%2
    return min(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
