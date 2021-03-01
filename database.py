from allotment_mechanism import * 
from csv import * 

mymachine= Allotment_machanism()
user= None
username= None

class Data:
      
    def __init__(self):
        self.vacancies={"Computer": 120, "IT": 60, "Mechanical": 60, "Electronics": 120}

        self.available_branches = ["Computer", "IT", "Mechanical", "Electronics"]

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
        global user, username
        user = usr
        username = usrnm


    def view_seatmatrix(self):
        print(self.seat_matrix)
        
        

    def find_record(self, name):
        with open("datasheet.csv",'r') as f:
            reader_object = reader(f)
            for row in reader_object:
                if(row[0]==name):
                    return 1
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
        if user==1:
            # for user= student, show only his record.(all columns)
            name = input("Enter your name: ")
            with open("datasheet.csv",'r') as f:
                reader_object = reader(f)
                for row in reader_object:
                    if(row[0]==name):
                    #print(f"This is the application status of {username}")
                         print(row)
            
        if user==2:
            # for user= admin, show details of any student
            print("input the name of a student to search their details")
            

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
        if self.find_record(username):
            if mymachine.allotment_done== True:
                print("Cannot Edit record now. Your allotment result is: ")
                # print allotment result
            else:
                #print("edit your record here") 
                name = input("Enter your name: ")
                with open("datasheet.csv",'r') as f:
                    reader_object = reader(f)
                    for row in reader_object:
                        if(row[0]==name):
                            to_edit= int(input(edit_menu))s
                            row[to_edit+2]= input("Enter new value:")
                            
                            
                print()
        else:
            print("Student Record not found. Please register yourself.")           

    def delete_record(self):
        #allow only if allotment is not yet done
        if self.find_record():
            if mymachine.allotment_done== True:
                print("Cannot withdraw the application now. Your allotment result is: ")
            else:
                confirmation = (input("Do you wish to remove your record permanently? (press 'y'/'n') "))
                if confirmation == 'y' :
                    print("Your application was removed from list")    
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

    

    student_options=[view_seatmatrix, register, search_student, edit_record, delete_record, view_cutoff_marks]
    admin_options=[mymachine.run_allotment, view_all_registrations, view_allotment_result, view_branchwise_allotment, search_student, students_without_allotment, vacancies_left]   
    

    