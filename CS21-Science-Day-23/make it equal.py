n, k = map(int, input().split())

heights = sorted(list(map(int, input().split())), reverse=True)

height = heights[0]
cost = 0
level = 0

for i in range(n):
    while heights[i] < height:
        height -= 1
        if cost + i > k:
            level += 1
            cost = i
        else:
            cost += i
if cost > 0:
    level += 1

print(level)