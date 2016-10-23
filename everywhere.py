n = int(input().strip())

ans = []
for i in range(n):
    unique = set()
    cities = int(input().strip())
    for j in range(cities):
        unique.add(input().strip())
    ans.append(len(unique))
[print(uc) for uc in ans]