bill=int(input("enter total bill:"))
goldmem=input("are you a gold member?:")
day=input("enter day:")
if(bill>1000 and goldmem=="yes" and (day=="saturday" or day=="sunday")):
    print("You got 20 percent off")
else:
    print("you dont have any offer")