add=lambda a,b:a+b
print(add(5,3))

num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,num))
print(even)

data=[
    {"name":"sameera","age":30},
    {"name":"sumehra","age":25}, 
    {"name":"varshini","age":35}
]
youngest_person=min(data,key=lambda x:x["age"])
print(youngest_person)
