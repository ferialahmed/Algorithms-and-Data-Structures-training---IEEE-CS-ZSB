import math
import os
import random
import re
import sys

# Complete the powerSum function below.

sub_arr = []
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        #print("sum(%s)=%s" % (partial, target))
        sub_arr.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])
    return len(sub_arr)
def powerSum(X, N):
    arr = [(int(math.pow(i,N))) for i in range(1,int(math.pow(X,1/N))+1)]
    return subset_sum(arr,X)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
