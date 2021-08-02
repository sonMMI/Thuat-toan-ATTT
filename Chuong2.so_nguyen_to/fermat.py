# chương trình kiểm tra tính nguyên tố fermat có a cho trước


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


def fermat(n, t, A):
    key = True
    for i in range(1, t + 1):    
        r = pow_repetition(A[i - 1], n-1, n)
        
        if r != 1:
            print('Co so a ={}: Hop so' .format(A[i - 1]))
            key = False
        else:
            print('Co so a ={}: Nguyen to' .format(A[i - 1]))
        
    if key == True:
        return print('{} co the la nguyen to'.format(n))
    else:
        return print('{} la hop so'.format(n))

if __name__ == '__main__':
    n = int(input('nhap n le & n >= 3, n = '))
    t = int(input('nhap t >=1, t = '))
    A = list()
    [A.append(int(i)) for i in input().split()]
    fermat(n, t, A)