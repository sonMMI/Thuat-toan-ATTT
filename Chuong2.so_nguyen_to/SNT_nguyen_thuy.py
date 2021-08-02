# # sàng eratosthenes
# # Số nguyên dương n

# # Quá trình tính sàng nguyên thủy để tìm tất cả các số nguyên tố ≤ n (theo mẫu). 
# # Trong các bước sàng, các phần tử được in ra dưới dạng <giá trị phần tử><2 khoảng trắng>.


def eratosthenes(n):
    arrTest = [True for i in range(n + 1)]

    p = 2
    print('Liet ke cac so nguyen tu 2 den {}'.format(n))
    for i in range(2, n+1):
        print(i, end='   ') if i != n else print(i)

    while (p <= n):
        if arrTest[p]==False:
            p+=1
            continue
        print('p=' + str(p))
        if (arrTest[p] == True):
            for i in range(p * p, n + 1, p):
                arrTest[i] = False
        for i in range(2, n+1):
            if arrTest[i]:
                print(i, end='  ') if i != n else print(i)
        p += 1
    print('Cac so nguyen to <= {}la:'.format(n))
    for i in range(2, n+1):
            if arrTest[i]:
                print(i, end='  ') if i != n else print(i)

if __name__ == '__main__':
    n = int(input())
    eratosthenes(n) 