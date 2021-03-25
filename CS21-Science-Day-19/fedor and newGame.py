n,m,k=input().split()
army_lst=list()
friends=0

for i in range(int(m)+1):
    army=int(input())
    army_lst.append((army))


for i in range(len(army_lst)-1):
    k_bits=0
    XOR=(army_lst[i])^(army_lst[int(m)])
    XOR=list(bin(XOR))

    k_bits=(XOR.count('1'))
    if (k_bits) <= (int(k)):
        friends+=1
print(friends)