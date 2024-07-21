# input: 1 cau 
# output: dem so chu cai va chu so trong cau do

s = str(input("nhap vao 1 cau: "))
noc =0
non=0
for i in s:
	if "0"<= i <='9': non +=1
	if "a"<=i<="z" or "A"<=i<="Z": noc +=1
print("So chu cai la: ",noc)
print("So chu so la: ",non)