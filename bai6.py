# input: so tien gui va so tien rut
# output: so tien thuc cua tai khoan ngan hang

d = list(map(int,(input("Nhap so tien rut: ").split())))
w = list(map(int,(input("Nhap so tien rut: ").split())))
s=0

for f in d:
	s += f
for k in w:
	s-=k
print("So tien thuc o trong tai khoan ngan hang la: ", s)