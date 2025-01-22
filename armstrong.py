num = int(input("Enter a number:"))
arm = 0
temp = num
for i in range(1,num+1):
    rem = num%10
    arm = arm + (rem**3)
    num = num//10
if(temp == arm):
    print("armstrong")
else:
    print("not armstrong")