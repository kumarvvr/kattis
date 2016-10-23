data = {}
data['A'] = [11,11]
data['K'] = [4,4]
data['Q'] = [3,3]
data['J'] = [20,2]
data['T'] = [10,10]
data['9'] = [14,0]
data['8'] = [0,0]
data['7'] = [0,0]

ip = [i for i in input().strip().split(' ')]
dom = ip[1]
length = int(ip[0])*4
score = 0
for i in range(length):
    inp = input().strip()
    if inp[1] == dom :
        score += int(data[inp[0]][0])
    else:
        score += int(data[inp[0]][1])
print(score)