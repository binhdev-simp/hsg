# input: so tu nhien
# # output: kiem tra co phai so hoan hao hay khong

n = int(input("Nhap vao so tu nhien: "))
s=0
for i in range(n):
    if n%(i+1)==0:
        s+=i+1
    if s == n: 
        print(str(n) + " la so hoan hao.")
        break