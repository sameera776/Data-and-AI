# def add_all(*args):
#     sum=0
#     for num in args:
#         sum=0
#         for num in args:
#             sum+=num
#         return sum
    
# print(add_all(1,2,3,4,5))

def print_data(**s):
    for key,val in s.items():
        print(f"{key}:{val}")

print_data(name="sameera",age=21)
