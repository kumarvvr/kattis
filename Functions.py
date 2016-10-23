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