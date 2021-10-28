z=90 # global variable 
def f1():
    y=90    # Local vraibale
    def f2():    # nested function 
        x=50     # non-local variable
        print("My x value=",x)
        print(y)
    f2()
    print("My x value=",x)
f1()

        
