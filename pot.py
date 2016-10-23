n = int(input().strip())
sum = 0
for i in range(n):
    val = str(input().strip())
    base = val[:-1]
    power = val[-1:]
    sum+=int(base)**int(power)
print(sum)