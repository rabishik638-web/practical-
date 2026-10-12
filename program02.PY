sname =["arun","ram","ravi","tamil"]
name =str(input ("Enter the  name :"))
flag =0
for na in sname:
    if na ==name:
        flag=1
        break
if (flag==1):
    print("given name is existing in the list")
else:
     print("given name is  not existing in the list")