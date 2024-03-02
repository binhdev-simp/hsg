#input: [2,4,..,100]
# output: tinh tong day so 2+4+6+...+100
# su dung while loop

i = 2
s=0
while i<=100:
	s+=i
	i+=2

print(s)