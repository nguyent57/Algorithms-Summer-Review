def prime_num(n):
    # IF THE NUMBER <= 1 RETURN, MUST START FROM 2
    if n <= 1:
        return False
    for i in range(2,n):
        if (n%i) == 0:
            return False
        else:
            return True
n=int(input())
while prime_num(n)!=True:
    n = int(input())
