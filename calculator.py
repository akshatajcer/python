def add(a,b):
    print(a+b)
def diff(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
print("welcome to my simple calculator")
print("enter the a and b value ")
a = int(input("enter the a value "))
b = int(input("enter the enter b value "))
print('''1)addition 
2)difference
3)divsion 
4)multiplication''')
choise = int(input("enter your choise "))
if choise == 1:
    add(a,b)
elif choise == 2:
    diff(a,b)
elif choise == 3:
    multi(a,b) 
elif choise == 4:
    div(a,b)   
 