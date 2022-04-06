from http.client import SWITCHING_PROTOCOLS


def message():
    # function body
    print("Hello ")

    age=int(input("Enter your age here "))
    name=input("Enter your name here ")
   
    if age>=18:
     print("Dev "+name+". You are "+str(age)+" years old")
    else:
     print(name+ " is ",str(age)+" years old")
message()

def calculator():
    num1=int(input("Enter a number of your choice "))
    num2=int(input("Enter a second number of your choice "))
    sum=num1+num2
    times=num1+num2
    div=num2/num1
    mod=num2%num1
    print("The summation of the numbers is ",+sum)
    print("The Multiplication of the numbers is ",+times)
    print("The Division of the numbers is ",+div)
    if mod==0:
        print("Both numbers are divible")
    elif mod==1:
        print(+num2,"One of the numbers is a prime number")
    else:
        print(+num1," and/or" +str(num2)," are old numbers")
calculator()