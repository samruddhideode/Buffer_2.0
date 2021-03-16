from allotment_mechanism import * 
from csv import * 
import time

mymachine= Allotment_machanism() #obj of class Allotment_machanism

# details of the user who is currently logged in. Initially set to Null.
user= None
name=""
pwd=None

class Data:
      
    def __init__(self):
        self.flag = 0  # flag=1: user has withdrawn his application, record is deleted from datasheet.

        # no. of vacant seats in each branch stored as dict. Initially all seats are vacant. This no. will reduce when each allotment is completed.
        self.vacancies={"Computer": 120, "IT": 60, "Mechanical": 60, "Electronics": 120}

        self.available_branches = ["Computer", "IT", "Mechanical", "Electronics"]

        # initially cutoffs for all branches are 0. These mks will be updated after entire allotment process is completed.
        self.cutoff_marks={"Computer": 0, "IT": 0, "Mechanical": 0, "Electronics": 0}

        self.seat_matrix= """
                SEAT MATRIX
    ---------------------------------------
    |     Branch         |      Vacancies |
    ---------------------------------------      
    |  1. Computer       |         120    |
    |  2. IT             |         60     |
    |  3. Mechanical     |         60     |
    |  4. Electronics    |         120    |
    ---------------------------------------
    """

        self.edit_menu= """
                WHAT DO YOU WANT TO EDIT?
    ---------------------------------------
    |     Option          |   Enter choice |
    ---------------------------------------      
    |  1. E-mail          |          0     |
    |  2. Preference1     |          1     |
    |  3. Preference 2    |          2     |
    |  4. Preference  3   |          3     |
    ---------------------------------------
    """

    def set_userinfo(self, usr, usrnm):
        # sets the info of the currently logged-in user in global variables user and name.
        global user, name
        user = usr
        name = usrnm
        self.flag=0 # set flag to 0 whenever a user logs in.

    def view_seatmatrix(self):
        # print total no. of seats available in each branch of college.
        print(self.seat_matrix)
        
        

    def find_record(self, name, pswd= None):
        with open("datasheet.csv",'r') as f:
            reader_object = reader(f)
            if pswd== None:
                for row in reader_object:
                    if(row[0]==name):
                        # return the row no. where record is found, password of that record
                        return reader_object.line_num, row[8]
            else:
                for row in reader_object:
                    if(row[0]==name) and row[8]==pswd:
                        # return the row no. where record is found
                        return reader_object.line_num
        # if record not found, return 0            
        return 0 
    
    def register(self):
        # search user name, if not found, create a new student record
        name = input("Enter your name: ")
        if self.find_record(name)==0:
            
            surname = input("Enter your surname: ")
            email = input("Enter your email: ")
            marks = int(input("Enter your marks: "))
            pref1 = int(input("Enter your preference 1: "))
            pref2 = int(input("Enter your preference 2: "))
            pref3 = int(input("Enter your preference 3: "))
            allotment = "--"
            record = [name, surname, email, marks, pref1, pref2, pref3, allotment]
        
            with open('datasheet.csv', 'a+', newline='') as f_object: 
    
                writer_object = writer(f_object) 
                writer_object.writerow(record) 
                f_object.close()
            
        else:
            print("You have registered successfully.")
            # print the student record    

    def view_all_registrations(self):
        # print table of all records (name, surname, email, marks)
        print("all registrations list")

    def view_allotment_result(self):
        if mymachine.allotment_done== False:
            print("Allotment is not yet done. Please check again later.")
        else:
            # print the rankwise result table (rank, name, surname, email, marks, allotment)
            print("allotment result table")

    def view_branchwise_allotment(self):
        # if allotment_done is T, input the branch name, print branchwise result list, else say that allotment is yet to be done.
        if mymachine.allotment_done== False:
            print("Allotment is not yet done. Please check again later.")
        else:
            branch= input("Enter branch name: ").capitalize()
            print(f"this is allotment result for {branch} engineering")
            # filter the result table for the inputted branch and display rank wise (rank, name, surname, email, marks, allotment)

    def search_student(self):
        if user==2:
            # for user= student, show only his record.(all columns)
            srname = input("Enter your surname: ")
            global name,pwd
            with open("datasheet.csv",'r') as f:
                reader_object = reader(f)
                for row in reader_object:
                    if(row[0]==name) and row[8]==pwd:
                        print("Applicant details: ")
                        for i in range(0,7):
                            print(row[i], end="   ")
                        return
            print("Sorry! No record found")            
            
        if user==3:
            # for user= admin, show details of any student
            # print("input the name of a student to search their details")
            name = input("Enter student name: ")
            srname= input("Enter student surname: ")
            with open("datasheet.csv",'r') as f:
                reader_object = reader(f)
                for row in reader_object:
                    if(row[0]==name) and row[1]==srname:
                        print("Applicant details: ")
                        for i in range(0,7):
                            print(row[i], end="   ")
                        return
            print("Sorry! No record found")            
            

    def get_cutoff_marks(self):
        # cutoff marks= in the rankwise sorted table, find last row of each branch. Corresponding marks of that row is cutoff marks.
        # store cutoff marks of each branch using for loop
        pass

    def view_cutoff_marks(self):
        # if allotment is done, display this table
        if mymachine.allotment_done== False:
            print("Allotment is not yet done. Please check again later.")
        else:
            self.get_cutoff_marks()
            print("cut off marks for each branch in a table are displayed") 
            for key, val in self.cutoff_marks.items():
                if key=="IT":
                    print(f"{key} :\t\t\t{val}")
                else:
                    print(f"{key} :\t\t{val}")

               

    def edit_record(self):
        #allow only if allotment is not yet done
        global name, pwd
        row_to_edit = self.find_record(name, pwd)
        if row_to_edit>0:
            if mymachine.allotment_done== True:
                print("Cannot Edit record now. Your allotment result is: ")
                # print allotment result
            else:
                print("edit your record here") 
                with open("datasheet.csv",'r') as f:
                    lines= f.read().splitlines()
                    
                    surname=(lines[row_to_edit]).split(",")[1]
                    email = input("Enter email: ")
                    marks = input("Enter marks: ")
                   
                    pref1 = input("Enter pref1: ")
                    pref2 = input("Enter pref2: ")
                    pref3 = input("Enter pref3: ")
                    allotment = "--"
                    lines[row_to_edit-1]=f"{name},{surname},{email},{marks},{pref1},{pref2},{pref3},'--',{pwd}"
                    
                with open("datasheet.csv",'w') as f:
                    # overwrite
                    for line in lines:
                        f.write(line+"\n")
                    
        else:
            print("Student Record not found. Please register yourself.")           



    def delete_record(self):
        #allow only if allotment is not yet done
        if mymachine.allotment_done== True:
            print(f"Cannot withdraw the application now. Your allotment result is: {self.find_record(name)}")
        else:    
            
            confirmation = (input("Do you wish to remove your record permanently? (press 'y'/'n') "))
            if confirmation == 'y' :
                # password= input("Enter your password: ")
                row_to_edit = self.find_record(name, pwd)
                if row_to_edit>0:
        
                    with open("datasheet.csv",'r') as f:
                        lines= f.read().splitlines()
                        del lines[row_to_edit-1]
                    with open("datasheet.csv",'w') as f:
                    # overwrite
                        for line in lines:
                            f.write(line+"\n")
                    print("Your application was removed from list")
                    self.flag=1
                else: 
                    return
            else:
                print("Student Record not found. Please register yourself.")           


    def students_without_allotment(self):
        # allow only after allotment is done
        if mymachine.allotment_done== False:
            print("Allotment is not yet done. Please check again later.")
        else:    
            print("list of students who were not alloted any seat.")

    def vacancies_left(self): 
        print("table of each branch and vacant seats left") 
        print(f"Branch\t\tVacancies left") 
        for key, val in self.vacancies.items():
            if key=="IT":
                print(f"{key} :\t\t\t{val}")
            else:
                print(f"{key} :\t\t{val}")
            
    
    def student_sign_up(self):
        name = input("Enter Your Name: ")
        surname=input("Enter your Surname: ")
        
        #check whether the person has already signed up
        with open ('datasheet.csv', 'r') as f_object: 
            reader_obj= reader(f_object)
            for row in reader_obj:
                if row[0]==name and row[1]==surname:
                    print(f"Account already exists for {name} {surname}.")
                    return

        # if they havent signed up already, ask them to set password and add a new record. 
        pswd = input("Set your password: ")
        with open('datasheet.csv', 'a+', newline='') as f_object: 
            writer_object = writer(f_object) 
            email = "--"
            marks = 0
            pref1 = -1
            pref2 = -1
            pref3 = -1
            allotment = "--"
            record = [name, surname, email, marks, pref1, pref2, pref3, allotment,pswd]
            writer_object.writerow(record) 
            f_object.close()
        print("\nYou have signed up successfully!")
        
    def check_pswd(self, name):
        #print("Welcome to pswd check",username)
        password = input("Enter your password: ")
        with open("datasheet.csv",'r') as f:
            reader_object = reader(f)
            for row in reader_object:
                if(row[0]==name) and row[8]==password:
                    global pwd
                    pwd= password
                    return(1)
        return 0 

    student_options=[view_seatmatrix, register, search_student, edit_record, delete_record, view_cutoff_marks]
    admin_options=[mymachine.run_allotment, view_all_registrations, view_allotment_result, view_branchwise_allotment, search_student, students_without_allotment, vacancies_left]   
    

    