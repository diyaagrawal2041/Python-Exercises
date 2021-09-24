# Factorial of a number using recursive method

def fact(n):
    if n<0:
        print("the factorial of negative numbers doesn't exist")
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

a=int(input("enter a number: "))
print("the factorial of ",a,"is ",fact(a))



# factorial of a number using iterative method
def fact(n):
    if n<0:
        print("the factorial of negative numbers doesn't exist")
    elif n==0 or n==1:
        return 1
    else:
        factorial=1
        while(n>1):
            factorial=factorial*n
            n-=1
        return factorial

a=int(input("enter a number: "))
print("the factorial of ",a,"is ",fact(a))
