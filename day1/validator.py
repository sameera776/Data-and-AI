email=input("enter email:")
password=input("enter password:")
if "@" not in email:
    print("invalid email")
elif(len(password)<6):
    print("invalid password")
else:
    print("valid credentials")