# p W
#a : mang
#b : mang

# in ra: ε,c
# trong đó ε là bit nhớ, c là mảng kết quả sao cho: c = a + b mod 2**(Wt)

from math import*

def summation(arrA, arrB, w, t):
    E = 0
    arrSum = []
    arrA = arrA[ : : -1]
    arrB = arrB[ : : -1]

    for t in range(t):
        sum = arrA[t] + arrB[t] + E
        mod = sum % (2 ** w)
        E = 1 if 2**w <= sum or sum < 0 else 0
        arrSum.append(mod)
    
    arrSum = arrSum[ : :-1]
    return E, arrSum

if __name__ == '__main__':
    p, w = [int(x) for x in input().split()]
    arrA = [int(x) for x in input().split()]
    arrB = [int(x) for x in input().split()]
    
    m = ceil(log2(p))
    t = ceil(m / w)

    E, arrSum = summation(arrA, arrB, w, t)
    print('A+B=(' + str(E) + ', [', end='')
    for i in range(len(arrSum)):
        print(arrSum[i], end='   ') if i != len(arrSum)-1 else print(arrSum[i], end='')
    print('])', end='')
