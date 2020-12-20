guests,guards=map(int,input().split())
doors=input()
dict={}
set=set()
for i in range(guests): O(N)
    dict[doors[i]]=i O(N)
for j in range(guests): O(N)
    set.add(doors[j]) O(N)
    if (len(set) > guards):
        print("YES")
        break
    if (j == dict[doors[j]]):
        set.remove(doors[j])
if (len(set) <= guards):
    print("NO")

Time complexity is O(N)
