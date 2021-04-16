planks, width = map(int, input().split())
heights=list(map(int, input().split()))
total = sum(heights[:width])
min = total
index = 1
for i in range (1, planks-width+1):
    total = total - heights[i-1] + heights[i+width-1]
    if total < min:
        min = total
        index = i+1
print(index)