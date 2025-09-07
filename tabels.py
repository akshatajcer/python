def tabel(no):
    for i in range (1,11):
     print(no, "*", i, "=", no*i)

def repeat(no):
   for i in range(no):
      print(f"this no repeated by {no} times")
print("welcome to my number system")
print('''choise 1 : tabels
choise 2 : repeat''')
choise = int(input("enter your choise "))
no = int(input("enter your no "))
if choise == 1:
    tabel(no)
elif choise == 2:
    repeat(no)