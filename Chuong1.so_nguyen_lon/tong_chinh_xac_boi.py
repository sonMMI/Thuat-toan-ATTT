# p W a b

# in ra: ε,c
# trong đó ε là bit nhớ, c là mảng kết quả sao cho: c = a + b mod 2**(Wt)

from math import*

def convert_to_array(x, w, t):
    arr = []

    for i in range(1, t + 1):
        tmp = 2 ** ((t - i) * w)
        index = x // tmp
        arr.append(index)
        x = x - (tmp * index)
    return arr

def summation(arrA, arrB, w, t):
    E = 0
    arrSum = []
    arrA = arrA[ : : -1]
    arrB = arrB[ : : -1]

    for i in range(t):
        sum = arrA[i] + arrB[i] + E
        mod = sum % (2 ** w)
        E = 1 if 2**w <= sum or sum < 0 else 0
        arrSum.append(mod)
    
    arrSum = arrSum[ : :-1]
    return E, arrSum

if __name__ == '__main__':
    # p = 2147483647
    # a = 38762497
    # b = 568424364
    # w = 8

    p, w, a, b = [int(x) for x in input().split()] 

    m = ceil(log2(p))
    t = ceil(m / w)

    arrA = convert_to_array(a, w, t)
    arrB = convert_to_array(b, w, t)
    E, arrSum = summation(arrA, arrB, w, t)
    print('A+B=(' +str(E) + ', [', end='')
    for i in range(len(arrSum)):
        print(arrSum[i], end='   ') if i != len(arrSum)-1 else print(arrSum[i], end='')
    print('])', end='')