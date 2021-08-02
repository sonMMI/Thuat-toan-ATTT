# -------Bài 1------
# chuyển số thành mảng
#--------input------
# p W a
#--------output------
# A=[A[t-1]   A[t-2]   ...   A[1]   A[0]]
# Các phần tử in cách nhau 3 khoảng trắng


from math import ceil, log2

def convert_to_array(p, w, a):
    m = ceil(log2(p))
    t = ceil(m/w)

    arr = []
    for i in range(1, t+1):
        tmp = 2 ** ((t-i) * w)
        index = a//tmp
        a = a - tmp*index
        arr.append(index)
    return arr

if __name__ == '__main__':
    p, w, a = [int(x) for x in input().split()]
    arr = convert_to_array(p, w, a)
    print('A= [', end='')
    for i in range(len(arr)):
        print(arr[i], end='   ') if i != len(arr)-1 else print(arr[i], end='')
    print(']', end='')