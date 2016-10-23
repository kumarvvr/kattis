ip = input().strip()

c = ip[0]
ans  = str(ip[0])
for i in range(len(ip)-1):
    if ip[i+1] != c:
        ans = ans+str(ip[i+1])
    c = ip[i+1]

print(ans)