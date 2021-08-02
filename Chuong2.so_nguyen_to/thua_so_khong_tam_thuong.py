# tìm một thừa số không tầm thường của một số n


def gcd(a, b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def pollards_rho(n):
    a = 2
    b = 2

    while True:
        a = (a**2 + 1) % n
        b = (b**2 + 1) % n
        b = (b**2 + 1) % n
        d = gcd(a - b, n)

        print('----------------------------------------------------------------')
        print('|%20d|%20d|%20d|'%(a,b,d))
        if(1 < d < n):
            return d
        if d == n:
            return False

if __name__ == '__main__':
    n = int(input('nhap n = '))
    print('----------------------------------------------------------------')
    print('|                   a|                   b|                   d|')
    result = pollards_rho(n)
    print('----------------------------------------------------------------')
    print('Thua so khong tam thuong cua {} la {}'.format(n, result))

