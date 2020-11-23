s=int(input(),2)
counter=0
i=0
while i>=0 and (2**(2*i))<s:
    i+=1
    counter+=1
print(counter)

