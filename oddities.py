n = int(input().strip())
ans = []
for i in range(n):
    num = int(input().strip())
    if (abs(num)%2 == 0):
        ans.append(str(num)+' is even')
    else:
        ans.append(str(num)+' is odd')

[print(i) for i in ans]