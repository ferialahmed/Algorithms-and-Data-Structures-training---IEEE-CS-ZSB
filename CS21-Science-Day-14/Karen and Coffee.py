noOfrecipes,minrecipes,quest=map(int,input().split()) O(N)
lst=[0]*(200005) 0(N)
count=0
for i in range(noOfrecipes):  0(N)
    l,r=map(int,input().split())
    lst[l]+=1
    lst[r+1]-=1
for j in range(1,len(lst)): O(N)
    lst[j]=lst[j-1]+lst[j]
for i in range(len(lst)):
    if lst[i]>=minrecipes:
        count+=1
    lst[i]=count
for i in range(quest):
    a,b=map(int,input().split())
    print(lst[b]-lst[a-1])
 Time complexity is O(N)