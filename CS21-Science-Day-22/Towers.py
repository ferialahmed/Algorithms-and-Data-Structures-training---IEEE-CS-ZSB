towers,op = map(int,input().split())
heights = list(map(int,input().split()))
opDescription = []
for i in range(op):
    maxIndex = heights.index(max(heights))
    minIndex = heights.index(min(heights))
    if minIndex != maxIndex:
        heights[maxIndex] -= 1
        heights[minIndex] += 1
        opDescription.append([maxIndex+1, minIndex+1])

print(max(heights)-min(heights),len(opDescription))
for j in opDescription:
    print(' '.join(map(str,j)))
