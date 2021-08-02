# Phép nhân
# p W a b

# in ra: c
# trong đó c là mảng kết quả thỏa mãn: c = a.b mod p

from math import*

#chuyen doi so -> mang arr
def convert_to_array(x, w, t):
    arr = []

    for i in range(1, t + 1):
        tmp = 2 ** ((t - i) * w) 
        index = x // tmp
        x = x - (tmp * index)
        arr.append(index)
    return arr

#phep toan nhan
def multiplication(arrA, arrB, t):
    arrMul = {}
    arrA = arrA[ : :-1]
    arrB = arrB[ : :-1]

    for i in range(t):
        arrMul[i] = 0
    for i in range(t):
        u = 0
        for j in range(t):
            uv = arrMul[i+j] + arrA[i] * arrB[j] + u
            u = uv // 256
            v = uv % 256
            arrMul[i+j] = v
        arrMul[i+t] = u
    arrMul_value = list(arrMul.values())
    arrMul_value = arrMul_value[ : :-1]
    return arrMul_value

if __name__ == '__main__':
    p, w = [int(x) for x in input().split()]

    m = ceil(log2(p))
    t = ceil(m / w)

    arrA = [int(x) for x in input().split()]
    arrB = [int(x) for x in input().split()]
    
    result = multiplication(arrA, arrB, t)
  
    print('c=a.b=[', end='')
    for i in range(len(result)):
        print(result[i], end='   ') if i != len(result) - 1 else print(result[i], end='')
    print(']')
