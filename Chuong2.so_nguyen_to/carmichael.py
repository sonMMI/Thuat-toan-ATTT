# carmichael

# ------input-----
# Dòng 1: t testcase
# t dòng tiếp theo mỗi dòng là một số nguyên n

from math import*

def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def pow_repetition(a, k, n):
    b = 1
    if k == 0:
        return b
    A = a
    if k & 1 == 1:
        b = a
    for i in range(1, len(bin(k)[2:])):
        A = (A**2) % n
        if (k >> i) & 1 == 1:
            b = A*b % n
    return b


def prime(n):
    if n < 2:
        return 0
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if(n % i == 0):
                return 0
        return 1

def isCarmichaelNumber(n):
    if(prime(n) == 1):
        return False
    for i in range(2,n):
        # nếu i là nguyên tố cùng nhau với n (UCLN = 1)
        if(gcd(i,n)==1):
            # và power của(i, n-1) %n != 1
            if(pow_repetition(i, n-1, n) != 1):
                return False
    return True

if __name__ == '__main__':
    t = int(input())
    nums = [0]*t
    for i in range(len(nums)):
        nums[i]=int(input())
    for i in nums:
        print('{} là số Carmichael'.format(i)) if isCarmichaelNumber(i) else print('{} không phải số Carmichael'.format(i))

    