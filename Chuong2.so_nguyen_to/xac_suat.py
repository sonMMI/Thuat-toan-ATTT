# ktra n có là SNT trong khoảng (a, b) cho trước
# --------input-------


from math import*
from random import randint

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

# thuật toán bình phương có lặp
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

# thuật toán tìm s và r
def find_R_S(n):
    s = 0
    n = n-1
    while n % 2 == 0:
        s += 1
        n /= 2
    return s, int(n)


def miller_rabin(n, s, r, aa, bb):
    flag = True

    # if n == 2 or n == 3:
    #     return True
    a = aa+1

    while a < bb:
        print('Co so a= {}:'.format(a))
        y = pow_repetition(a, r, n)
        if y != 1 and y != n-1:
            print('y= {} => (y!=1)&&(y!=n-1)'.format(y))
        j = 1
        print('   j=1')
        while j <= s-1 and y != n-1:
            y = (y**2) % n
            if y == 1:
                flag = False
                print('Ket qua: Hop so')
                a += 1
                continue
            print('   j={}, y={} =>(j<=s-1)&&(y!=n-1)'.format(j, y))
            j += 1
        if y != n-1:
            flag = False
            print('y = {} => y!=n-1'.format(y))
            print('Ket qua: Hop so')
            a += 1
            continue
        print('Ket qua: Nguyen to')
        a += 1
    print('{} co the la nguyen to'.format(n)) if flag else print('{} la hop so'.format(n))

if __name__ == '__main__':
    n = int(input())
    a, b = [int(x) for x in input().split()]
    print('Kiem tra so nguyen n={}:'.format(n))
    s, r = find_R_S(n)
    print('{}-1 = 2^{}.{}'.format(n, s, r))
    miller_rabin(n, s, r, a, b) 

