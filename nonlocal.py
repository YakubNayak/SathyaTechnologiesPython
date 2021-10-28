def outer():
    x = "local"   # local variable
    print("outer:", x)
    def inner():   # nested function 
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
   

outer()


