a,b = map(int, input("nhap 2 so a, b: ").split())
c=0
def check(x):
    if x<1 or x<10: return False #khong co so raone thoa man
    elif x==1: return True #chi co so 1 la so raone thuoc (0;10)
    else:
        i=0
        t=0
        while x!=0:
            i+=1
            if i%2==0:t+=x%10
            else: t-=x%10
            x=x//10
        if t==1: return True
        if t!=1: return False
if 0<a<b:
    for i in range(a,b+1):
        if check(i)==True: c+=1
    print([a,b],"co",c,"so Ra-one")
