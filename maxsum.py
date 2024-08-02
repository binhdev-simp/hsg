import math
import time
n = int(input(''))
st = time.time()
begin = n-round(math.sqrt(n))
end = n-1
l = {(math.gcd(n,m)+m) : m for m in range(begin,end)}
kq = str(l[max(l)])
ed = time.time()
print(kq,':',max(l))
print('Time run:',ed-st)