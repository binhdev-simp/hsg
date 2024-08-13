f = open("sums.inp", 'r')
ff = open("sums.out", 'w')
n = int(f.readline())
s=0
if 1 <= n <= 10**9:
    for i in range(1,n+1):
        t= (i+1)**2 - i**2
        s+=t
ff.write(str(s))
f.close()
ff.close()