# trừ trên Fp
# p W a b

# in ra: c
# trong đó c là mảng kết quả thỏa mãn: c = a - b mod p

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
    arrC = []
    arrA = arrA[ : :-1]
    arrB = arrB[ : :-1]

    for i in range(t):
        sub = arrA[i] - arrB[i] - E
        mod = sub % (2 ** w)
        E = 1 if (2 ** w) <= sub or sub < 0 else 0
        arrC.append(mod)
    arrC = arrC[ : :-1]
    return E, arrC

def summation(arrC, arrP, w, t):
    E = 0
    arrCNew = []
    arrC = arrC[ : :-1]
    arrP = arrP[ : :-1]

    for i in range(t):
        sum = arrC[i] + arrP[i] + E
        mod = sum % (2 ** w)
        E = 1 if (2 ** w) <= sum or sum < 0 else 0
        arrCNew.append(mod)
    arrCNew = arrCNew[ : :-1]
    return arrCNew

def subtraction_Fp(arrC, arrCNew, E):
    if(E == 1):
        return arrCNew
    else:
        return arrC

if __name__ == '__main__':
    p, w, a, b = [int(x) for x in input().split()]

    m = ceil(log2(p))
    t = ceil(m / w)

    arrP = convert_to_array(p, w, t)
    arrA = convert_to_array(a, w, t)
    arrB = convert_to_array(b, w, t)
    
    E, arrC = subtraction(arrA, arrB, w, t)
    arrCNew = summation(arrC, arrP, w, t)

    result = subtraction_Fp(arrC, arrCNew, E)
    print('[', end='')
    for i in range(len(result)):
        print(result[i], end='   ') if i != len(result) - 1 else print(result[i], end='')
    print(']', end='') 