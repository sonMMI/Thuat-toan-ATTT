from random import randint


def findR_S(n):
    dem = 0
    n = n-1
    while n % 2 == 0:
        dem += 1
        n /= 2
    return dem, int(n)


def modular_pow(a, k, n):
    if k == 0:
        return 1
    b = 1
    A = a
    if k & 1 == 1:
        b = a
    for i in range(1, len(bin(k)[2:])):
        A = (A**2) % n
        if (k >> i) & 1 == 1:
            b = A*b % n
    return b


def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a


def miller_rabin(n, t=5):
    s, r = findR_S(n)
    arrRand = []
    for i in range(1, t+1):
        a = randint(2, n-2)
        while a in arrRand:
            a = randint(2, n-2)
        arrRand.append(a)
        if gcd(a, n) != 1:
            return False
        else:
            y = modular_pow(a, r, n)
            if y != 1 and y != n-1:
                j = 1
                while j <= s-1 and y != n-1:
                    y = (y**2) % n
                    if y == 1:
                        return False
                    j += 1
                if y != n-1:
                    return False
            return True


def pollard_rho(n, c=5):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 5 == 0:
        return 5
    elif n % 7 == 0:
        return 7
    elif miller_rabin(n):
        return n
    a = 2
    b = 2
    while True:
        a = (a**2+c) % n
        b = (b**2+c) % n
        b = (b**2+c) % n
        d = gcd(abs(a-b), n)
        if 1 < d and d < n and miller_rabin(d):
            return d
        if d == n:
            # a = 2
            # b = 2
            # c -= 1
            return pollard_rho(n, c-1)


def analyze(n):
    coSo = list()
    soMu = list()

    while n != 1:

        dem = 0
        i = pollard_rho(n)
        while n % i == 0 and i != 1:
            dem += 1
            n //= i
        if dem > 0:
            coSo.append(i)
            soMu.append(dem)
    return coSo, soMu

if __name__== '__main__':
    n=int(input())
    cs, sm = analyze(n)
    print('n = {} = '.format(n),end='')
    for i in range(len(cs)):
        print('{}^{}'.format(cs[i],sm[i]),end='')
        if i!=len(cs)-1:
            print(' + ',end='')