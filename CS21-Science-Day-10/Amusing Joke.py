text1=input() O(1)
text2=input() O(1)
text3=input() O(1)
text1=text1+text2 O(n)
if len(text1)==len(text3):O(1)
    if all(text3.count(i)==text1.count(i) for i in (text3)): O(n)
            print("YES") O(1)
    else:
        print("NO")
else: O(1)
    print("NO") O(1)

Time complexity is O(n^2)
