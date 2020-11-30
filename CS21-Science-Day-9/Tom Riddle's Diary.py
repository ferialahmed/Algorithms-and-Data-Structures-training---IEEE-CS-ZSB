numberOfpeople=int(input())      1
names=[]                         1
for i in range(numberOfpeople):  n+1
    letters=input()              n
    names.append(letters)        n
for i in range(numberOfpeople):  n+1
    if all(names[j]!=names[i] for j in range(i-1,-1,-1)):  n
        print("NO")                                         n
    else:
        print("YES")                                       n


Then time of complexity is 0(n)
