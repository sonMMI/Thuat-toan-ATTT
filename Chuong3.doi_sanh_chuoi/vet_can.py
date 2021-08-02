# thuật toán vét cạn
def vetcan(T, P):
    dem = 0
    for i in range(len(T)-len(P) + 1):
        k = i
        for j in range(len(P)):
            dem += 1 
            if T[k] == P[j]:
                if j == len(P)-1:
                    return True, i, dem
                k += 1
            else:
                break
    return False, i, dem

if __name__ == '__main__':
    P = input()
    T = input()
    check, i, dem = vetcan(T, P)
    if check == True:
        print('su xuat hien cua mau "{}" trong van ban "{}" co vi tri bat dau la {}, so phep lap la {}'.format(P, T, i, dem))
    else:
        print('mau "{}" khong xuat hien trong van ban "{}", so phep lap la {}'.format(P, T, dem))

