
# hàm tiền xử lí mẫu P, 
def lastOccurrence(T,P):
    A = sorted(set(T))
    L = {}
    for i in A:
        L[i] = P.rfind(i)
    return L

def boyer_moore(T, P):
    L = lastOccurrence(T,P)
    dem = 0
    j = len(P)-1
    i = j
    m = len(P)
    
    print('\tT va P')
    while i < len(T):
        dem += 1
        print(str(dem) + ':\t' + str(T[i]) + ' va ' + str(P[j]))
        if T[i] == P[j]:
            if j == 0:
                return True, dem, i
            i = i-1
            j = j-1
        else:
            i = i+m-min(j, 1+L[T[i]])
            j = m-1
    return False, dem, i

if __name__ == "__main__":
    
    P = str(input('mẫu P: '))
    T = str(input('mẫu T: '))
    check, dem, i = boyer_moore(T, P)
    if check == True:
        print('sự xuất hiện của mẫu "{}" trong văn bản "{}" có vị trí bắt đầu là {}'.format(P, T, i) )
        print('số phép lặp là: {}'.format(dem))
    else:
        print('mẫu "{}" không xuất hiện trong văn bản "{}"'.format(P, T))
        print('số phép lặp là: {}'.format(dem))


