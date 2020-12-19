squares=int(input()) O(1)
numbers=list(map(int,input().split())) O(n)
ways=0 O(1)
pre=[] O(1)
pre.append(numbers[0]) O(1)
for i in range(1,squares): O(n)
    pre.append(pre[i-1]+numbers[i]) O(n)

for i in range(len(pre)-1): O(n)
    if pre[i]==pre[len(pre)-1]-pre[i]: O(n)
        ways+=1
print(ways) O(1)
Time complexity is O(n)