length=int(input()) O(1)
text=input().lower() O(1)
text=set(text) O(n)
if len(text)==26:O(1)
    print("YES") O(1)
else:
    print("NO")

Time complexity is O(n)