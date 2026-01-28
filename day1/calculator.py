def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter ur choice\n 1.add \n 2.sub \n 3.mul \n 4.div \n"))
if(c==1):
    print(add(a,b))
elif(c==2):
    print(sub(a,b))
elif(c==3):
    print(mul(a,b))
elif(c==4):
    print(div(a,b))
