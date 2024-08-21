f = open ("bnum.inp","r")
ff =open("bnum.out",'w')
n = int(f.readline())
def ktnt(x):
	if x < 10 and x in [1,2,3,5,7]: return True
	if x >= 10 and x % 2 !=0:
		for i in range(3,round(x**0.5)+1,2):
			if x % i == 0: return False
		else: return True
	else: return False
	return True
if 10<=n<=10**18: 
	s=0
	while n != 0:
		s+=(n-(n//10)*10)**2
		n=n//10
	if ktnt(s)==True:
		ff.write(str(1)+'\n')
		ff.write(str(s))
	else:
		ff.write(str(-1)+'\n')
		ff.write(str(s))
f.close()
ff.close()