# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is running")
        result = func(*args, **kwargs)
        print("Function has finished")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(3, 5))
