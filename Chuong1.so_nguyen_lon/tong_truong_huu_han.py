# cộng trên Fp
# p W a b

# in ra: c
# trong đó c là mảng kết quả thỏa mãn: c = a + b mod p


from math import ceil, log2

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
    arrC = []
    arrA = arrA[ : :-1]
    arrB = arrB[ : :-1]

    for i in range(t):
        sum = arrA[i] + arrB[i] + E
        mod = sum % (2 ** w)
        E = 1 if (2 ** w) <= sum or sum < 0 else 0
        arrC.append(mod)
    arrC = arrC[ : :-1]
    return E, arrC

def subtraction(arrC, arrP, w, t):
    E = 0
    arrCNew = []
    arrC = arrC[ : :-1]
    arrP = arrP[ : :-1]

    for t in range(t):
        sub = arrC[t] - arrP[t] - E
        mod = sub % (2 ** w)
        E = 1 if (2 ** w) <=sub or sub < 0 else 0
        arrCNew.append(mod)
    arrCNew = arrCNew[ : :-1]
    return arrCNew

def comparison(arrC, arrP):
    for i in range(len(arrC)):
        if arrC[i] > arrP[i]:
            return True
        elif arrC[i] < arrP[i]:
            return False
        else:
            if i == len(arrC) - 1:
                return True
            continue

def summation_Fp(arrC, arrCNew, E):
    if(E == 1):
        return arrCNew
    else:
        if(comparison):
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

    E, arrC = summation(arrA, arrB, w, t)
    arrCNew = subtraction(arrC, arrP, w, t)

    result = summation_Fp(arrC, arrCNew, E)
    print('[', end='')
    for i in range(len(result)):
        print(result[i], end='   ') if i != len(result) - 1 else print(result[i], end='')
    print(']', end='')
    

