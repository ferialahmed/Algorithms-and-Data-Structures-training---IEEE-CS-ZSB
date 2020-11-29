numberOfsnacks=int(input())               
snacksSize=list(map(int,input().split()))  
listOfsize=set()                           
maxsize=max(snacksSize)                    
for i in range(len(snacksSize)):           
    listOfsize.add(snacksSize[i])           
    while maxsize in listOfsize:            
        print(maxsize,end=" ")              
        maxsize-=1
    print('')




