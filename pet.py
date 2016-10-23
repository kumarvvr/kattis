max = 0
n = 0
for i in range(5):
    s = sum([int(i) for i in input().strip().split(' ')])
    if s> max :
        max = s
        n = i

print(n+1,max) 
