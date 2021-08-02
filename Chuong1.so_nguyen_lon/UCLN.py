# # tim UCLN của hai số nguyên không âm a, b (a≥b>0)

# # Input:
# # 2
# # 420 429
# # 134 550

# # Output:
# # 3
# # 2

def UCLN(a, b):
    if b > a:
        tmp = a
        a = b
        b = tmp

    if b == 0:
        d = a
        x = 1
        y = 0
        return d

    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1

    while b > 0:
        q = a // b
        r = a - q*b
        x = x2 - q*x1
        y = y2 - q*y1

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    
    d = a
    x = x2
    y = y2

    return d

if __name__ == '__main__':
    t=int(input())
    result=[0]*t
    for i in range(len(result)):
        a,b = [int(x) for x in input().split()]
        result[i]=UCLN(a,b)
    for i in result:
        print(i)