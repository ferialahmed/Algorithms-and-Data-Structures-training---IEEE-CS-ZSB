import collections
arr=[98 ,67 ,35 ,1 ,74 ,79 ,7 ,26, 54 ,63 ,24 ,17 ,32 ,81]
array=collections.deque(arr)
array.rotate(-10)
print(' '.join(str(i) for i in array))
