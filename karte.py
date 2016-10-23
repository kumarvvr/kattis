ip = input().strip()
ncards = len(ip)/3
l=[]
for i in range(len(ip))[0::3]:
    l.append(ip[i:i+3])


suits = set()
cards=set()
scr = [0,0,0,0]
for item in l:
    cards.add(item)
    suits.add(item[0])
    if(item[0] == 'P'): scr[0] += 1
    if(item[0] == 'K'): scr[1] += 1
    if(item[0] == 'H'): scr[2] += 1
    if(item[0] == 'T'): scr[3] += 1

if(len(cards) != ncards):
    print('GRESKA')
else:
    ans = [(a-b) for a,b in zip([13,13,13,13],scr)]
    [print(card) for card in ans]