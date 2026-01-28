# def profile(**data):
#     print("Profile Details:")
#     for key,value in data.items():
#         print(f"{key}:{value}")

# nm=input("enter name:")
# ag=int(input("enter age:"))
# phno=input("enter mobile no:")
# mail=input("enter email:")
# profile(name=nm,age=ag,phone_no=phno,email=mail)



def profile(**data):
    result=""
    for key,value in data.items():
        result+=f"{key}:{value}\n"
    return result

nm=input("enter name:")
ag=int(input("enter age:"))
phno=input("enter mobile no:")
mail=input("enter email:")
print(profile(name=nm,age=ag,phone_no=phno,email=mail))