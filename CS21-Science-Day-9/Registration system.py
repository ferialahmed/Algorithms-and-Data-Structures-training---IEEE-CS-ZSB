Numrequests=int(input())     1
lstOfrequests={}             1
for i in range(Numrequests):  n+1
    requests=input()           n
    if requests in lstOfrequests:  n
        lstOfrequests[requests]+=1  n
        prompt=requests+str(lstOfrequests.get(requests))  n
        print(prompt)    n
    else:                 n
        lstOfrequests[requests]=0    n
        print("OK")                  n

Then time of complexity is O(n)


