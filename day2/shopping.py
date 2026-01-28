lst=[]
while True:
    str=input("enter item:")
    if(str!="done"):
        lst.append(str)
    else:
        break
for i in lst:
    print(i)