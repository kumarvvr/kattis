t = 1440
ip = input().strip().split(' ')
ts = int(ip[0]) * 60 + int(ip[1])
ts -= 45
m = ts%60
h = int((ts-m)/60)
if h<0:
    h = 24+h
print(h,m)