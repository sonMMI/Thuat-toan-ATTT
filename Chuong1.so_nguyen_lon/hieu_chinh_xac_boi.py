# p W a b

# input: ε,c
# trong đó ε là bit nhớ, c là mảng kết quả sao cho: c = a - b mod 2Wt

from math import*

def convert_to_array(x, w, t):
    arr = []

    for i in range(1, t + 1):
        tmp = 2 ** ((t - i) * w)
        index = x // tmp
        arr.append(index)
        x = x - (tmp * index)
    return arr

def subtraction(arrA, arrB, w, t):
    E = 0
    arrSub = []
    arrA = arrA[ : :-1]
    arrB = arrB[ : :-1]

    for i in range(t):
        sub = arrA[i] - arrB[i] - E
        mod = sub % (2 ** w)
        E = 1 if (2 ** w) <= sub or sub < 0 else 0
        arrSub.append(mod)

    arrSub = arrSub[ : :-1]
    return E, arrSub

if __name__ == '__main__':
    # p = 2147483647
    # a = 38762497
    # b = 568424364
    # w = 8

    p, w, a, b = [int(x) for x in input().split()]
    m = ceil(log2(p))
    t = ceil(m/ w)
    
    arrA = convert_to_array(a, w, t)
    arrB = convert_to_array(b, w, t)

    E, arrSub = subtraction(arrA, arrB, w, t)
    print('c=a-b=('+ str(E) + ', [', end='')
    for i in range(len(arrSub)):
        print(arrSub[i], end='   ') if i != len(arrSub)-1 else print(arrSub[i], end='')
    print('])', end='')
