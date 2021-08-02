# euclide nghịch đảo

# Mỗi dòng có một số nguyên lớn không âm tương ứng p và a

# In ra: giá trị nghịch đảo a^-1 mod p.
# ------------ ------- ------
# input:
# 489573857
# 45682375

# Output:
# 45682375^-1 mod 489573857 = 242160691

def euclideND(a, p):
    u = a 
    v = p
    x2 = 0
    x1 = 1

    while(u != 1):
        q = v // u
        r = v - (q*u)
        x = x2 - (q*x1)

        v = u
        u = r
        x2 = x1
        x1 = x
    return x1 % p
     
if __name__ == '__main__':
    p = int(input())
    a = int(input())

    result = euclideND(a,p)
    print('{}^-1 mod {} = {}'.format(a, p, result))