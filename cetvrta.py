
xlist = []
ylist = []
xset = set()
yset = set()

def numDuplicates(l,n):
    return len([1 for x in l if x==n])

for i in range(3):
    a,b = input().strip().split(' ')
    xlist.append(a)
    ylist.append(b)
    xset.add(a)
    yset.add(b)
xset = list(xset)
yset = list(yset)
ans = []
ans.append(xset[1]) if (numDuplicates(xlist,xset[0]) == 2) else ans.append(xset[0])
ans.append(yset[1]) if (numDuplicates(ylist,yset[0]) == 2) else ans.append(yset[0])
print(ans[0],ans[1])