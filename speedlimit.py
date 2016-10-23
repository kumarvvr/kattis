n = 0
res = []
while True:
    n = int(input().strip())
    if n == -1:
        break
    speed = []
    time = []
    miles = 0
    #print("n is ",n)
    for i in range(n):
        ip = input().strip().split(' ')
        #print("ip is ",ip)
        speed.append(int(ip[0]))
        time.append(int(ip[1]))
        if i == 0:
            miles = speed[0]*time[0]
        else:
            miles += speed[i]*(time[i]-time[i-1])
    res.append(str(miles)+' miles')
[print(x) for x in res]