import math

h,v = [int(x) for x in input().strip().split(' ')]
print(math.ceil( h / (math.sin(math.radians(v)))))