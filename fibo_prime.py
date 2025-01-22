def prime_number(b):
    if(b<=1):
        print("not prime")
    else:
        for i in range(2,b):
            if(b%i==0):
                return False
            else:
                return True





def fibonacci(num):
    if(num == 0):
        return 0
    elif(num == 1):
        return 1
    else:
        a=0
        b=1
        for i in range(0,num-2):
            c = a+b
            
            a = b
            b = c

    return c






num = int(input("Enter your number:"))
fib = fibonacci(num)
print(fib)
if(prime_number(fib)):
    print("prime")
else:
    print("not prime")