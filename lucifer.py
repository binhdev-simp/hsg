import math
a,b = map(int, input("Nhap 2 so a,b (a<b):").split())
c=0
#kiem tra so nguyen to:
def ktnt(n):
    if n <10:
        if n in [2,3,5,7]: return True
    if n >=10:
        if n%2==0: return False
        u=3#bat dau voi uoc = 3
        maxu=round(n**1/2)#uoc lon nhat ma n co the chia den
        while u<maxu+1: #range(u,maxu+1)
            if n%u==0: return False
            else: u+=2
            # Neu n chia het cho u => n khong phai so nguyen to
            # Neu n khong chia het cho u => u+=2 vi snt khong co nghiem chan
        else: return True

for i in range(a, b+1):
    t=0
    e=0#kiem tra vi tri chan le cua so
    while i!=0:
        e+=1#init cho vi tri bat dau la vi tri le (aka hang don vi)
        if e%2==0: t+=i%10
        else:t-=i%10
        i=i//10
        if ktnt(t)==True: c+=1
print("Co",c,"so Lucifer trong doan",[a,b])