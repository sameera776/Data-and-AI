# import threading
# import time
# # def say_hello():
#     print("hello world")

# t=threading.Thread(target=say_hello)
# t.start()

# print("MAin Thread")

# def task():
#     print("task started")
#     time.sleep(2)
#     print("task completed")
# task()
# print("Program finished")


# import threading
# def greet(name):
#     print(f"Hello, {name}!")
# t=threading.Thread(target=greet,args=("Alice",))
# t.start()

# import time

# def greet(name):
#     time.sleep(2)   
#     print(f"Hello, {name}!")

# greet("Alice")


#multiple threading
import threading
def worker(num):
    print(f"Worker {num} is running")
    time.sleep(1)
    print(f"Worker {num} has finished")
    
for i in range(5):
    t=threading.Thread(target=worker,args=(i,))
    t.start()


#api with threading
import urllib.request
import threading
import time
import json
import ssl
def download_json():
    try:
        print("connecting to api")
        time.sleep(2) 
        url='https://fakestoreapi.com/products'
        headers={
            "User_Agent":"Mozilla/5.0"
        }
        req=urllib.request.Request(url,headers=headers)
        context=ssl._create_unverified_context()
        with url.request.urlopen(req,context=context)as response:
            data=response.read()
        print("Data downloaded")
    # data=urllib.request.urlopen(url).read()
    # data=urllib.request.urlretrieve(url,'filename')
    # time.sleep(2)
        posts=json.loads(data)
        with open('posts.json','w')as f:
            json.dump(posts,f,indent=4)

        print("download complete")
    except Exception as e:
        print("Error:",e)

t=threading.Thread(target=download_json)
t.start()
print("Main thread continues execution")

