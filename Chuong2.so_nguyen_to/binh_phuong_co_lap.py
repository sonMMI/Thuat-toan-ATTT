# bình phương có lặp
# -----input-----
# Dòng 1: số nguyên dương n
# Dòng 2: số nguyên a
# Dòng 3: số nguyên dương k
# ------output------
# In ra quá trình tính nhân bình phương có lặp theo mẫu

def pow_repetition(a, k, n):
    print('chuyen {} sang nhi phan: {}' .format(k, bin(k)[2:]))
    b = 1
    if k == 0:
        return b
    A = a
    print('Dat A = a = {}' .format(a))
    if k & 1 == 1:
        b = a
    for i in range(1, len(bin(k)[2:])):
        A = (A**2) % n
        print('Dat A = A^2 = %d' %A)
        if (k >> i) & 1 == 1:
            b = A*b % n
            print('- K_{} = 1, dat b = b*A mod {} = {}'.format(i, n, b))

    return b

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    k = int(input())
    b = pow_repetition(a, k, n)
    print('=> {}^{} mod {} = {}'.format(a, k, n, b))