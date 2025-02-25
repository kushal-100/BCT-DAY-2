def sub(x,y):
    return(x-y)
def add(x,y):
    return(x+y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return (x/y)
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
operation1=input("choose the operation 1.+ \n 2.- \n 3.* \n 4./ \n")
if operation1=='1':
    a=add(num1,num2)
    print(a)
elif operation1=='2':
    a=sub(num1,num2)
    print(a)
elif operation1=='3':
    a=mul(num1,num2)
    print(a)
elif operation1=='4':
    a=div(num1,num2)
    print(a)    
       
