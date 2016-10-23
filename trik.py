start = [1,0,0]

def swap(config,data):
    if(config =='A'):
        data[1],data[0] = data[0],data[1]
    elif (config == 'B'):
        data[2],data[1] = data[1],data[2]
    else:
        data[2],data[0] = data[0],data[2]

[swap(x,start) for x in list(input().strip())]
[print(x+1) for x in range(3) if start[x]==1]