# input: so tu nhien n
# output: n!! va n! voi n!! = tich cac so le tu 1-n, n! = tich cac so chan tu 2-n
n = int(input("Nhap so tu nhien n: "))
n1=1
n2=1
for i in range(1, n+1):
    if i%2==0: n1*=i
    else: n2*=i
print("n! =", n1)
print("n!! =", n2)