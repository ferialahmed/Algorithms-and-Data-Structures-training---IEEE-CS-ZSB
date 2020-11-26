n,k=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(chr(ord("a")+i%k))
result_str = ''.join(i for i in lst)
print(result_str)
