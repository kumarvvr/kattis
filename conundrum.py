ip = input().strip()

days = 0

for i in range(len(ip))[0::3]:
    if(ip[i] != 'P'): days+=1
    if(ip[i+1] != 'E') : days+=1
    if(ip[i+2] != 'R') : days+=1
print(days)