import itertools,collections

inp = input().strip().split(' ')
out = []
for w in inp:
    iw = ''
    iterator = range(len(w)).__iter__()
    for i in iterator:
        cursor = w[i]
        iw = iw + cursor
        if cursor in ['a','e','i','o','u']:
            collections.deque(itertools.islice(iterator,2))
    out.append(iw)
[print(o) for o in out]