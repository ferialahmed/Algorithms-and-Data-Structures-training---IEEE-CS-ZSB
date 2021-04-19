myName = input()
actions = int(input())
factors = {'commented': 10, 'posted': 15, 'likes': 5}
dict = {}
for i in range(actions):
    action = input().split()
    if action[0] == myName:
        dict[action[-2].replace('\'s', '')] = dict.get(action[-2].replace("\'s", ''), 0) + factors[action[1]]
    elif action[-2].replace("\'s", "") == myName:
        dict[action[0]] = dict.get(action[0], 0) + factors[action[1]]
    else:
        dict[action[0]] = dict.get(action[0],0)
        dict[action[-2].replace("\'s", "")] = dict.get(action[-2].replace("\'s", ''), 0)

sortedDict = sorted(dict,  key=lambda k: (-dict[k], k))
for i in sortedDict:
    print(i)
