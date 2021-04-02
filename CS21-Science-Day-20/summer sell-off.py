n,f =map(int,input().split())
z=0
a=[]
for i in range(n):
    products,clients=map(int,input().split())
    z+=min(products,clients)
    a.append(min(2*products,clients)-min(products,clients))
a.sort()
print(z+sum(a[n-f:]))
print(a[n-f:])
