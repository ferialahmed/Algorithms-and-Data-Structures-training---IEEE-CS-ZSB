numOfstones=int(input()) O(1)
cost=list(map(int,input().split())) O(n)
costCopy=cost[:]  O(n)
costCopy.sort() O(nlogn)
questions=int(input()) O(1)
pre1=[]
pre2=[]
pre1.append(cost[0])
pre2.append(costCopy[0])
for i in range(1,numOfstones): O(n)
    pre1.append(pre1[i-1]+cost[i]) n*O(1)
    pre2.append(pre2[i-1]+costCopy[i]) n*O(1)

for i in range(questions): O(n)
    type,l,r=map(int,input().split()) O(n)
    if type==1: n*O(1)
        if l!=1: n*O(1)
            print(pre1[r-1]-pre1[l-2]) n*O(1)
        else:
            print(pre1[r-1])
    if type==2:
        if l!=1:
            print(pre2[r - 1] - pre2[l - 2])
        else:
            print(pre2[r-1])

Time complexity is O(nlogn)
