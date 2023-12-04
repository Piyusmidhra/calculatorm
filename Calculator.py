print('''
  + ADD
  - SUBSTRACT   
  * MULTIPLY   
  / DEVIDE  
 ''')
num1=int(input("Enter the value1:-"))
num2=int(input("Enter the value2:-"))
opr=input("Enter the Opr..(+,-,*,/)")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid Opr....")