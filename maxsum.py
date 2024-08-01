import math
n = int(input("nhap so n: "))
c=0
gcdSum=0
tpm=0
def gcd(x,y):
    return math.gcd(x,y)
#main
if 3<=n<=10**14:
    for m in range(1,n):
        gcdSum = gcd(m,n)+m
        if gcdSum >= tpm:
            if gcdSum>tpm:
                tpm = gcdSum
            if m>c: c=m
        print(gcdSum, tpm,m,c, gcd(m,n))
# print(tpm)