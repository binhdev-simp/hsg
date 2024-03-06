# input: tram bo co, tram con bo, bo dung an 5 bo, bo nam an 3 bo, 3 con con lai an 1 bo
# output: so trau moi loai

for i in range(1, 21) :
    for j in range(1, 34) :
        k= 100 - i - j
        if 5*i + 3*j + k/3 == 100 :
            print( "Bò đứng ",i," bò nằm ",j," bò già ",k)