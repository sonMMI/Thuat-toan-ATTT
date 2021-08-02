# thuật toán Knuth - Morris - Pratt

# tìm tiền tố
def find_prefix(n, P):
    tt = []
    s = ''
    for i in range(n): # 0 -> j-1
        s = s + P[i]
        tt.append(s)
    return list(reversed(tt))

#tìm hậu tố 
def find_suffixes(n, P):
    ht = []
    s = ''
    for i in range(n-1, 0, -1):# 1 -> j-1 //vì phải -> trái: end - 1(1-1 = 0)
        s = P[i]+s
        ht.append(s)
    return list(reversed(ht))

# hàm tiền xử lí mẫu failure
def failure(P):
    F = [0]*len(P)
    F[0] = -1
    for j in range(1, len(F)):

        tt = find_prefix(j, P)
        ht = find_suffixes(j, P)

        for i in tt:
            try:
                ht.index(i)
                F[j] = len(i)
                if F[j] != 0:
                    break
            except:
                continue
    return F


def kmp(T, P):
    F = failure(P)
    i = 0
    j = 0
    dem = 0
    while i + j < len(T):
        dem += 1
        print(str(dem) + ':\t' + str(T[i+j] + ' và ' + str(P[j])))
        if T[i + j] == P[j]:
            j += 1
            if j == len(P):
                return True, dem, i
        elif T[i + j] != P[j]:
            i = i + j - F[j]
            if F[j] == -1:
                j = 0
            else:
                j = F[j]
    return False, dem, i

if __name__ == '__main__':
    P = 'aba'
    T = 'abbabac'
    check, dem, i = kmp(T, P)
    if check == True:
        print('sự xuất hiện của mẫu \"' + P + '\" trong văn bản \"' + T + '\" có vị trí bắt đầu là ' + str(i))
        print('số phép lặp làm: ' + str(dem))
    else:
        print('mẫu \"' + P + '\" không xuất hiện trong văn bản \"' + T + '\"')
        print('số phép lặp là: ' + str(dem))
