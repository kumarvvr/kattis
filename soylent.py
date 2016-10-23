ip = int(input().strip())
res = []
for x in range(ip):
    n = int(input().strip())
    if n % 400 != 0:
        res.append(int(n/400)+1)
    else:
        res.append(int(n/400))
[print(X) for X in res]