import datetime

''' DEFAULT TASK'''

t=datetime.datetime.now()
tskdetd={"Name":"default",
         "Description":"first default task",
         "Created_at":"2024-06-04 10:33",
         "Updated_at":t}
lot=[tskdetd]

'''CHOICE FUNCTIONS'''

def create():
    print("Please enter the details for the new task")
    tname=input("Enter the name: ")
    tdesc=input("Enter the description: ")
    t=datetime.datetime.now()
    tskdet={"Name":tname,
            "Description":tdesc,
            "Created_at":t,
            "Updated_at":t}
    lot.append(tskdet)
    for i in lot:
        print(i)
    more=input("Would you like to add another task?(y/n): ")
    if more=="y":
        create()
    elif more=="n":
        main()
    else:
        print("Invalid Input")
        main()

def view():
    print("Here are the tasks that exist")
    for i in lot:
        print(i)
    main()
    
def edit():
    print("Here are the tasks that can be edited")
    for i in range(len(lot)):
        print(f"{i}:{lot[i]}")
    
    num=int(input("Enter the number of the task in which you would like to make changes: "))
    
    if 0<=num <len(lot):
        task=lot[num]
        print(f"Selected task: {task}")
        editoption={1:"Name",2:"Description"}
        e=int(input('''What would you like to edit?
                1.Name
                2.Description
                3.Exit
                Choice_'''))
        
        if e==1:
            upname=input("Enter the updated name: ")               #edit name in dict
            task["Name"]=upname
            task["Updated at"]=datetime.datetime.now()
            print("Here is the updated task",task)

        elif e==2:
            updesc=input("Enter the updated description: ")        #edit desc in dict
            task["Description"]=updesc
            task["Updated at"]=datetime.datetime.now()
            print("Here is the updated task",task)

        elif e==3:
            main()
        else:
            print("Invalid input")

    else:
        print("Invalid task number")
    main()

def dlt():
    print("Here are the tasks that can be deleted")
    for i in range(len(lot)):
        print(f"{i}:{lot[i]}")

    dtask=int(input("Enter the number of the task which you would like to delete: "))

    if 0<=dtask <len(lot):
        print(f"Deleted task: {lot[dtask]}")
        del lot[dtask]
        print("Task deleted successfully")                                           #delete the dict at that number
    else:
        print("Invalid task number")
    main()

'''MAIN FUNCTION'''

def main():
    print("""   THIS IS A TODO LIST
      Choose from the options given below
      1. Create a new task
      2. View a task
      3. Edit a task
      4. Delete a task
      5. Exit""")
    
    tin=int(input("Enter the choice: "))

    if tin==1:
        # everytime clicked new dict should be made
        create()

    elif tin==2:
        view()
        # view task

    elif tin==3:
        edit()
        # edit task

    elif tin==4:
        dlt()
        # delete task

    elif tin==5:
        print("You have exited the program")
        exit()
        # exit
        
    else:
        print("Invalid Input")
        main()
    
    
if __name__=='__main__':
    main() 