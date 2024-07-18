import datetime

t=datetime.datetime.now()
reg_stu={'Name':"Ram",
         'Mobile':5546384563,
         'Address':"Jaipur",
         'Class':11,
         'Subject':"Arts",
         'Obtained_marks':75}
los=[reg_stu]

subl={'Subject Name':"CompSci",
      'Max_marks':100}
losub=[subl]

markl={'Subject Name':"Arts",
       'Max_marks':100,
       'Obtained_marks':50}
lomark=[markl]

'''STUDENT CLASS'''

class Student:
    print("This is the student registry")
    
    def view_stu(self):
        print("This the list of registered students")
        for i in los:
            print (i)
        main()

    def create_stu(self):
        print("Enter the details of the student")

        stuname=input("Enter the name: ")
        stumob=input("Enter the mobile number: ")
        
        while len(stumob) != 10 or (not stumob.isdigit()):
            print ("Not a 10 digit number")
            stumob = input("Please enter your 10 digit number:")
        
        stuadd=input("Enter the address: ")
        stuclass=int(input("Enter the class (1-12): "))   
        
        while stuclass < 1 or stuclass > 12:
            print("Invalid class number")
            stuclass = int(input("Enter the class (1-12): "))

        stusub=input("Enter the subject: ")
        
        reg_stu={'Name':stuname,
                 'Mobile':stumob,
                 'Address':stuadd,
                 'Class':stuclass,
                 'Subject':stusub,
                 'Created_at':t,
                 'Updated_at':t}
        los.append(reg_stu)
        main()
        
    def update_stu(self):
        print("Update the entry of a registered student")
        for i in range(len(los)):
            print(f"{i}:{los[i]}")

        stu_num=int(input("Enter the number associated with the student: "))
        
        if 0 <= stu_num <len(los):
            stu=los[stu_num]
            print(f"Selected student: {stu}")

            ust=int(input('''What would you like to update?
                        1.Name
                        2.Mobile
                        3.Address
                        4.Class
                        5.Subject
                        6.Obtained Marks
                        7.Exit
                        Choice->'''))
            
            if ust==1:
                upname=input("Enter the updated name: ")
                stu['Name']=upname
                stu['Updated_at']=datetime.datetime.now()
                print("Here is the updated name:",stu)

            elif ust==2:
                upmob=int(input("Enter the updated mobile no.: "))
                
                while len(upmob) != 10 or (not upmob.isdigit()):
                    print ('Not a 10 digit number')
                    upmob = int(input('Please enter your 10 digit number:'))
                
                stu['Mobile']=upmob
                stu['Updated_at']=datetime.datetime.now()
                print("Here is the updated mobile no.:",stu)

            elif ust==3:
                upadd=input("Enter the updated address: ")
                stu['Address']=upadd
                stu['Updated_at']=datetime.datetime.now()
                print("Here is the updated address:",stu)

            elif ust==4:
                upclass=int(input("Enter the updated class (1-12): "))      #update class input
                stu['Class']=upclass
                stu['Updated_at']=datetime.datetime.now()
                print("Here is the updated class:",stu)

            elif ust==5:
                upsub=input("Enter the updated subject: ")
                stu['Subject']=upclass
                stu['Updated_at']=datetime.datetime.now()
                print("Here is the updated class:",stu)

            elif ust==6:
                main()

            else:
                print("Invalid input")
        
        else:
            print("Invalid number of the student")
        main()

    def delete_stu(self):
        print("Here are the number of the students that can be deleted")
        for i in range(len(los)):
            print(f"{i}:{los[i]}")

        dstu=int(input("Enter the number of the student which you would like to delete: "))

        if 0 <= dstu <len(los):
            print(f"Deleted student record: {los[dstu]}")
            del los[dstu]
            print("Student record deleted successfully")
        else:
            print("Invalid number")
        # main()

'''SUBJECT CLASS'''

class Subject(Student):
    print("This is the subject registry")

    def view_sub(self):
        print("This the list of existing subjects")
        for i in los:
            print (i)
        main()

    def create_sub(self):
        print("Enter the details of the subject")
        subname=input("Enter the name of the subject: ")
        submaxmark=int(input("Enter the maximum marks: "))

        subl={'Subject Name':subname,
              'Max_marks':submaxmark,
              'Created_at':t,
              'Updated_at':t}
        losub.append(subl)
        main()
        
    def update_sub(self):
        print("Update the entry of a subject")
        for i in range(len(losub)):
            print(f"{i}:{losub[i]}")

        sub_num=int(input("Enter the number associated with the subject: "))

        if 0<= sub_num <len(losub):
            sub=losub[sub_num]
            print(f"Selected subject: {sub}")

            usub=int(input('''What would you like to update?
                        1.Subject Name
                        2.Maximum Marks
                        3.Exit
                        Choice->'''))
            
            if usub==1:
                upsubname=input("Enter the updated subject name: ")
                sub['Subject Name']=upsubname
                sub['Updated_at']=datetime.datetime.now()
                print("Here is the updated subject name:",sub)

            elif usub==2:
                upsubmark=int(input("Enter the updated subject max marks: "))
                sub['Max_marks']=upsubmark
                sub['Updated_at']=datetime.datetime.now()
                print("Here is the updated subject name:",sub)

            elif usub==3:
                main()

            else:
                print("Invalid input")

        else:
            print("Invalid number of the subject")
        main()

    def delete_sub(self):
        print("Here is the list of subjects that can be deleted")
        for i in range(len(losub)):
            print(f"{i}:{losub[i]}")

        dsub=int(input("Enter the number associated with the subject you wish to delete: "))

        if 0 <= dsub <len(losub):
            print(f"Deleted subject: {losub[dsub]}")
            del losub[dsub]
            print("Subject deleted successfully")
        else:
            print("Invalid number")
        main()

'''MARKS CLASS'''

class Marks(Student):
    print("This is the marks registry")
    
    def view_mark(self):
        print("This the list of marks")
        for i in los:
            print (i)
        main()

    def create_mark(self):
        print("Enter the details of the marks")
        msubname=input("Enter the name of the subject: ")
        maxmark=int(input("Enter the maximum marks: "))
        markobt=int(input("Enter the maximum marks obtained: "))

        subl={'Subject Name':msubname,
              'Max_marks':maxmark,
              'Obtained_marks':markobt,
              'Created_at':t,
              'Updated_at':t}
        lomark.append(markl)
        main()
        
    def update_mark(self):
        print("Update the entry of marks")
        for i in range(len(losub)):
            print(f"{i}:{losub[i]}")

        mark_num=int(input("Enter the number associated with the subject: "))

        if 0<= mark_num <len(lomark):
            marks=lomark[mark_num]
            print(f"Selected subject: {marks}")

            umark=int(input('''What would you like to update?
                        1.Subject Name
                        2.Maximum Marks
                        3.Obtained marks
                        4.Exit
                        Choice->'''))
            
            if umark==1:
                updsubname=input("Enter the updated subject name: ")
                marks['Subject Name']=updsubname
                marks['Updated_at']=datetime.datetime.now()
                print("Here is the updated subject name:",marks)

            elif umark==2:
                upmaxmark=int(input("Enter the updated max marks: "))
                marks['Max_marks']=upmaxmark
                marks['Updated_at']=datetime.datetime.now()
                print("Here is the updated subject name:",marks)

            elif umark==3:
                upobmark=int(input("Enter the updated Obtained marks: "))
                marks['Max_marks']=upobmark
                marks['Updated_at']=datetime.datetime.now()
                print("Here is the updated subject name:",marks)
            
            elif umark==4:
                main()

            else:
                print("Invalid input")

        else:
            print("Invalid number of the marks")
        main()

    def delete_mark(self):
        print("Here is the list of marks that can be deleted")
        for i in range(len(lomark)):
            print(f"{i}:{lomark[i]}")

        dmark=int(input("Enter the number associated with the subject marks you wish to delete: "))

        if 0 <= dmark <len(lomark):
            print(f"Deleted marks: {losub[dmark]}")
            del losub[dmark]
            print("Marks deleted successfully")
        else:
            print("Invalid number")
        main()

'''OBJECT'''

stu=Student()
sub=Subject()
mark=Marks()

'''MAIN'''

def main():
    print("""   THIS IS A STUDENT MANAGEMENT PROGRAM
      Choose from the options given below
      1. STUDENTS
      2. SUBJECTS
      3. MARKS
      4. Exit""")
    
    smin=int(input("Enter the choice: "))

    if smin==1:
        print('''Choose from the options given below
                1. Register a new student
                2. View student list
                3. Update student details
                4. Delete registered student
                5. Exit''')
        stuin=int(input("Enter the choice: "))

        if stuin==1:
            stu.create_stu()

        elif stuin==2:
            stu.view_stu()

        elif stuin==3:
            stu.update_stu()

        elif stuin==4:
            stu.delete_stu()

        elif stuin==5:
            print("You have exited the program")
            exit()

        else:
            print("Invalid input")
            main()

    elif smin==2:
        print('''Choose from the options given below
                1. Register a new subject
                2. View subject list
                3. Update subject details
                4. Delete registered subject
                5. Exit''')
        subin=int(input("Enter the choice: "))

        if subin==1:
            sub.create_sub()

        elif subin==2:
            sub.view_sub()

        elif subin==3:
            sub.update_sub()

        elif subin==4:
            sub.delete_sub()

        elif subin==5:
            print("You have exited the program")
            exit()

        else:
            print("Invalid input")
            main()


    elif smin==3:
        print('''Choose from the options given below
                1. Register marks
                2. View marks list
                3. Update marks details
                4. Delete registered marks
                5. Exit''')
        markin=int(input("Enter the choice: "))

        if markin==1:
            mark.create_mark()

        elif markin==2:
            mark.view_mark()

        elif markin==3:
            mark.update_mark()

        elif markin==4:
            mark.delete_mark()

        elif markin==5:
            print("You have exited the program")
            exit()

        else:
            print("Invalid input")
            main()


    elif smin==4:
        print("You have exited the program")
        exit()
        
    else:
        print("Invalid Input")
        main()
    
    
if __name__=='__main__':
    main() 