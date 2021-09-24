def fib(n):
    a=0
    b=1
    if n < 0:
        print("Please enter a positive integer")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        # return fib(n-1) + fib(n-2)
        print("Fibonacci sequence: ")
        print(a)
        print(b)
        for i in range(1,n):
            c=a+b
            a,b=b,c
            print(b)
            i = i + 1

x=int(input("enter the number of fibonacci sequence: "))
print(fib(x))
