n,m=map(int,input().split()) O(1)
arrA=list(map(int,input().split())) O(n)

reversedArray=set()
count=[]
for i in range(n-1,-1,-1): O(n)
    reversedArray.add(arrA[i]) n*O(1)
    count.append(len(reversedArray))  n*O(1)

for i in range(m): O(m)
    L = int(input()) m*O(1)
    print(count[-L]) m*O(1)
Time complexity is O(n)




