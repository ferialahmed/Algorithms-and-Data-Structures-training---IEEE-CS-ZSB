n=int(input())
noOfbacteria=0
while(n>=1):
    if (n%2)==1:
        n-=1
        noOfbacteria+=1
    else:
        n/=2
print (noOfbacteria)