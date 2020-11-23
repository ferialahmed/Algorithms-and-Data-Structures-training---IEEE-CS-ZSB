import os
def largestRectangle(h):
    lst=[]
    n=len(h)
    counter=1
    for i in range(n):
        for j in range(i+1,n):
            if h[i]<=h[j]:
                counter+=1
            else:
                break
        for x in range(i-1,-1,-1):
            if h[i]<=h[x]:
                counter+=1
            else:
                break
        lst.append(h[i]*counter)
        counter = 1
    return max(lst)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

