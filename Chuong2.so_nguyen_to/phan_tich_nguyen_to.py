from math import*

def phanTich(n):
    snt = []
    soMu = []

    for i in range(2, n+1):
        dem = 0
        while n % i == 0:
            dem += 1
            n /= i
        if dem > 0:
            snt.append(i)
            soMu.append(dem)
        if n == 1:
            break
    return {'snt': snt, 'soMu': soMu}
        
if __name__ == '__main__':
    n = int(input('nhap n: '))
    coSo = phanTich(n).get('snt')
    soMu = phanTich(n).get('soMu')
    
    print('n = '+ str(n) + ' = ', end='')
    for i in range(len(coSo)):
        x = coSo[i]
        y = soMu[i]
        print(str(x) + '^' +str(y), end='')
        if i < (len(coSo) - 1):
            print(' + ', end='')
