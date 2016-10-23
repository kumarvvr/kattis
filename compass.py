present = int(input().strip())
target =  int(input().strip())

print((target-present)) if ((target-present)<180) else print('-',360- (target-present))