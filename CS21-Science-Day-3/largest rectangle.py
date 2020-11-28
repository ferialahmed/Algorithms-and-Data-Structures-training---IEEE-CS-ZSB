import os
def largestRectangle(h):
    lst=[]          1
    n=len(h)        1
    counter=1       1
    for i in range(n):   n+1
        for j in range(i+1,n):  n(n-i)
            if h[i]<=h[j]     n(n-i)
                counter+=1     n(n-i)     
            else:              1
                break
        for x in range(i-1,-1,-1):  
            if h[i]<=h[x]:
                counter+=1
            else:                1
                break
        lst.append(h[i]*counter) n
        counter = 1              n
    return max(lst)              1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

    Then time complexity is O(n^2)
