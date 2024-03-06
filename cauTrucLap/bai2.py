# input: cac so co 3 chu so abc
# output: cac so thoa man a^3 + b^3 + c^3 = abc

for i in range(100, 1000):
    a = i//100
    b = (i - a*100)//10
    c = i - a*100 -b*10
    if pow(a,3) + pow(b,3) + pow(c,3) == i: print(str(i)+'\n')