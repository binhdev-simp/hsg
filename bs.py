f = open('input.inp', 'r')
ff = open ('output.out', 'w')
n,x = map(int, f.read().split())
init=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if j*i==x:
            init+=1
ff.write(str(init))
f.close()
ff.close()