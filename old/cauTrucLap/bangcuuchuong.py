# input: cac so tu 1-9
# output: bang cuu chuong

for i in range(1, 10):
    print("bang nhan " + str(i))
    for j in range(1, 10):
        print(str(i) + "x" +str(j)+"="+str(i*j))
    print('\n')  