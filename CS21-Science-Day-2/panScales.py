scalesWeights=(input())
weights=(input())
delimiter=scalesWeights.find("|")
left=scalesWeights[:delimiter]
right=scalesWeights[delimiter+1:]
for i in weights:
    if len(left)<=len(right):
       left=left+i
    else:
        right=right+i

if len(left)==len(right):
    print(left+"|"+right)
else:
    print("Impossible")


