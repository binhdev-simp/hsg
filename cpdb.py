f = open('input.inp','r')
ff = open ('output.out','w')
m, n = map(int, f.read().split())
c=0
def ktnt(x):
    if x < 10:
        if x not in [2,3,5,7]: return False
    elif x>=10: 
        if x%2==0: return False
        else: 
            for i in range(3,round(x**0.5),2):
                if x%i ==0: return False
                else:return True
for i in range(round(m**0.5),round(n**0.5)+1):
    if ktnt(i):
        c+=1
print(c)
f.close()
ff.close()