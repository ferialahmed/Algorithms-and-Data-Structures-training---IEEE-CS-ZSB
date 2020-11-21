from fractions import Fraction
no1,no2=list(map(int,input().split()))
Max=max(no1,no2)
prob=6-Max+1
if prob==6:
    print("1/1")
elif prob==0:
    print("0/1")
else:
    print(Fraction(prob,6))
