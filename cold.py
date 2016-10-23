import sys
n = input() # Discard the first input. 
print(len([1 for x in input().strip().split(' ') if int(x) < 0]))