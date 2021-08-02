# sàng eratosthenes
# n m
# Trong đó m là kích cỡ phân đoạn

# Quá trình tính sàng nguyên thủy để tìm tất cả các số nguyên tố ≤ n (theo mẫu). 
# Trong các bước sàng, các phần tử được in ra dưới dạng <giá trị phần tử><2 khoảng trắng>.

import math

def sangNguyenThuy (array, n):
    for i in range(2, n):
        if array[i] == 1:
            for j in range(2*i, n, i):
                if array[j] == 1:
                    array[j] = 0
            print("p=%d" % i)
            for a in range(2, n):
                if array[a] == 1:
                    print(a, end="  ")
            print()


def sangPhanDoan(array, n, tmp):
    limit = 0
    count = 0
    print("Chia pham vi tu 2 den %d thanh cac doan co kich co %d" %(n,tmp))
    for a in range(2, len(array)):
        if count == tmp:
            print("||", end="")
            count = 0
        print(a, end="  ")
        count += 1
    print()
    print("Xet doan 1:")
    sangNguyenThuy(array, 2+tmp)
    count = 2
    for i in range(2 + 2*tmp, len(array) + 1, tmp):
        print("Xet doan %d:" %count)
        count += 1
        for j in range(2, int(math.sqrt(i))+1):
            if array[j] == 1:
                for k in range(i - tmp, i):
                    if array[k] == 1:
                        if k % j == 0:
                            array[k] = 0
                print("p=%d" % j)
                for a in range(i - tmp, i):
                    if array[a] == 1:
                        print(a, end="  ")
                print()
        limit = i
    if limit != len(array):
        print("Xet doan %d:" % count)
        for j in range(2, int(math.sqrt(limit))+1):
            if array[j] == 1:
                for k in range(limit, len(array)):
                    if array[k] == 1:
                        if k % j == 0:
                            array[k] = 0
                print("p=%d" % j)
                for a in range(limit, len(array)):
                    if array[a] == 1:
                        print(a, end="  ")
                print()
    print("Tat ca cac so nguyen to <= %d:" %n)
    for a in range(2, len(array)):
        if array[a] == 1:
            print(a, end="  ")


if __name__ == '__main__':
    inp = input()
    tm = inp.split()
    n = int(tm[0])
    tmp = int(tm[1])
    a = [1]*(n+1)
    sangPhanDoan(a, n, tmp)