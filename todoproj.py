import datetime

''' DEFAULT TASK'''

t=datetime.datetime.now()
tskdetd={"Name":"default",
         "Description":"first default task",
         "Created_at":"2024-06-04 10:33",
         "Updated_at":t}
det1={"ID":1,"Task":tskdetd}
tsk={"Task1":det1}
lot=[tskdetd]

'''INTERFACE'''

print("""   THIS IS A TODO LIST
      Choose from the options given below
      1. Create a new task
      2. View a task
      3. Edit a task
      4. Delete a task
      5. Exit""")
# tin=int(input("Enter the choice: "))

'''CASES'''
def taskman():
    global tskdet,tin
    if tin==1:
        # everytime clicked new dict should be made
        def var():
            global tskdet
            tname=str(input("Enter the name: "))
            tdesc=str(input("Enter the description: "))
            tskdet={"Name":tname,
                    "Description":tdesc,
                    "Created_at":t,
                    "Updated_at":t}
        def crtsk(tname,tdesc):
            return tskdet
        lot.append(tskdet)
        # for i in lot:
        #     print(i)
        ad=str(input("Would you like to add another task?(y/n): "))
        if ad=="y":
            var()
        elif ad=="n":
            pass
        else:
            print("Invalid Input")
            pass
    elif tin==2:
        for i in lot:
            print(i)
    # view task
    elif tin==3:
        pass
    # edit task
    elif tin==4:
        pass
    # delete task
    elif tin==5:
        pass 
    # exit
    else:
        print("Invalid Input")

tin=int(input("Enter the choice: "))
taskman()