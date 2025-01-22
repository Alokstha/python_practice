def fibo(num):
    if num<=1:
        return num
    else:
        return(fibo(num-1)+fibo(num-2))


num = int(input("Enter a number:"))
if(num<=0):
    print("Enter a positive number")
else:
    for i in range(0,num):
        print(fibo(i))