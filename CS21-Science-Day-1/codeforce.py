from fractions import Fraction
no1,no2=list(map(int,input().split())) O(1)
Max=max(no1,no2)                       O(1)
prob=6-Max+1                           O(1)
if prob==6: O(1)
    print("1/1") O(1)
elif prob==0: O(1)
    print("0/1") O(1)
else: O(1)
    print(Fraction(prob,6)) O(1)
    
    
 Then time complexity is O(1)
