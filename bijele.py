import sys
target = [1,1,2,2,2,8]
data = [int(x) for x in input().strip().split(' ')]
res = [str(target[r] - data[r]) for r in range(len(target))]
print(' '.join(res))