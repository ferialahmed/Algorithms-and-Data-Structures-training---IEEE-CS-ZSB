import os
import collections
def rotateLeft(d, arr):
    array=collections.deque(arr) O(1)
    array.rotate(-d)    O(d)
    return array O(1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w') 

    first_multiple_input = input().rstrip().split() 

    n = int(first_multiple_input[0]) 

    d = int(first_multiple_input[1]) 

    arr = list(map(int, input().rstrip().split())) 

    result = rotateLeft(d, arr) 

    fptr.write(' '.join(map(str, result))) 
    fptr.write('\n')

    fptr.close() 
    
    Then time complexity is O(1)

