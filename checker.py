n = int (input("Nhap n: "))
e = str(input("Nhap cac chu so bi loi: "))
count=0
for i in range(1,n+1):
    for j in list(str(i)):
        if j in list(e) : 
            count+=1
            break
print(n-count)