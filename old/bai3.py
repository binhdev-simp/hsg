# input:[1000; 3000]
# output: cac so chan in ra thanh chuoi tren 1 dong cach nhau boi dau phay
r = ""
for i in range(1000,3001):
	if i%2==0: r += str(i) + ', '
print(r[:len(r)-2])