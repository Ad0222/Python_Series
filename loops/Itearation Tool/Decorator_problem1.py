import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start}time")
        return result 
    return wrapper

@timer
def hello():
    print("hello")
@timer
def example_function(n):
    time.sleep(n)
    
hello()
example_function(2)