def add(Tasks):
     task_name = input("enter you task ")
     Tasks.append({"task":task_name,"status":"pending"})
def   view(Tasks):
     if not Tasks:
          print("tasks are not there")
     else:
       for i, Task in enumerate(Tasks,1):
            print(f" {i}. {Task['task']} - {Task['status']} " )
def   marktask(Tasks):
     if not Tasks:
         print("task are not marked as completed")
     else:
          print("which task do you want to mark as completed")
          for i , Task in enumerate(Tasks,1):
               print(f" {i}. {Task['task']} - {Task['status']} ")
          num = int(input("enter your task to marke as completed "))
          if 1<=num<=len(Tasks) :
               Tasks[num-1]["status"]="completed"
               print("Task marked as completed!")
def   delete(Tasks):
    if not Tasks:
        print("task are not there to delete")
    else:
        for i ,Task in enumerate(Tasks,1):
            print(f"{i}. {(Task['task'])}-{(Task['status'])}")
        N = int(input("enter your task number which you wants to delete "))
        if 1 <= N <= len(Tasks):
         remove = Tasks.pop(N-1)
         print(f" you have succesfully removed {remove['task']} from the tasks")
Tasks=[]
while True:
    print("Welcome to my TO-DO app")
    print("1.Adding Task")
    print("2.View all Task")
    print("3.mark as complited")
    print("4.Delete Task")
    print("5c.Exit from app")
    choice =input("Enter your choice ")
    if choice == "1":
     add(Tasks)
    elif choice == "2":
        view(Tasks)
    elif choice == "3":
        marktask(Tasks)
    elif choice == "4":
        delete(Tasks)
        
    else:
        print("Exit from our app")
cle
                     
               
               
     



















