
    
    
#hello()


def myfunc(func):
    print("orginal function")
    func()
    
    
#myfunc(hello)

@myfunc
def hello():
    print("hello world!")
    