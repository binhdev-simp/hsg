# input: n, k (n > k)
# output: nCk
def myfn():
    global k
    global ban
    k = int(input("Nhap k: "))
    ban = int(input("Nhap n: "))
    n1 =1
    k1=1
    minusNandK =1 
    for i in range(1, ban+1): n1*=i
    for j in range(1, k+1): k1*=j
    for f in range(1, (ban-k)+1): minusNandK *= f
    nCk = n1/(k1*(minusNandK))
    print("To hop chap nCk=", nCk)
myfn()
if ban>k: myfn()