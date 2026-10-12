n = int (input ("Enter your first value :"))
m = int (input ("Enter your lost value :"))
print ( "prime number are :  ",end ="")
for i in range(n ,m+1):
    flag=0
    for j in range (2,i):
        if i%j ==0:
            flag=1
            break
    if flag==0:
           
      print (i,end=" ")