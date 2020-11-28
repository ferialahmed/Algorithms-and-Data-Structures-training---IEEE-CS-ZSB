scalesWeights=(input()) 1
weights=(input())        1
delimiter=scalesWeights.find("|")  1
left=scalesWeights[:delimiter]     1
right=scalesWeights[delimiter+1:]   1
for i in weights:             weights+1
    if len(left)<=len(right):   weights
       left=left+i               weights
    else:                           
        right=right+i            weights

if len(left)==len(right):        1
    print(left+"|"+right)         1
else:                              1
    print("Impossible")             1
    
    
    Then time complexity is O(n)


