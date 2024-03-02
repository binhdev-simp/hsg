# input:cac so nguyen tu 2000 den 3200
# output: cac so chia het cho 7 khong chia het cho 5 moi so cach nhau boi dau phay
res = ""
for i in range(2000, 3201):
	if i %7==0 and i%5!=0:
		res= res+ str(i)+', '
print(res[:(len(res)-2)])

