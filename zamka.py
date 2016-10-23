
l = int(input().strip())
d = int(input().strip())
c = int(input().strip())

def sumDigits(n):
    # Function to compute the sum of digits of a number.
    if n<10:
        return n
    else :
        sum=0

        while n>0:
            sum += n% 10
            n //= 10
    return sum

for x in range(d-l):
    if(sumDigits(x+l) == c):
        print(x+l)
        break

for x in range(d-l):
    if(sumDigits(d-x) == c):
        print(d-x)
        break
