# building a calculator

num1=float(input("enter the value of the num1 :"))
op=input("enter the type of operation :")
num2=float(input("enter the value of the num2 :"))
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1 / num2)
else:
    print("no operation")