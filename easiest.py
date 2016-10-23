from Functions import *

inp = []

while True:
    dat = int(input().strip())
    if dat == 0:
        break
    else:
        inp.append(dat)

for i in inp:
    # Iterate through the list
    s = 11
    while True:
        tar = i * s
        if(sumDigits(i) == sumDigits(tar)):
            print(s)
            break
        s+=1