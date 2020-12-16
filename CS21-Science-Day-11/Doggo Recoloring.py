numOfpuppies=int(input()) O(1)
colors=input() O(1)
colorset=set(colors) O(n)
if len(colors)==1:   O(1)
    print("YES")     O(1)
else:
    for i in colorset: O(n)
        if colors.count(i)>=2: n*O(n)
            print("YES")    n*O(n)
            break
    else:
        print("NO")

Time complexity is O(n^2)