from allotment_mechanism import *
import json
from csv import *

mymachine= Allotment_machanism()
user= None
user_name= None
firstname=None

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


    def set_userinfo(self, usr, usrnm, fname):
        global user, user_name, firstname
        user = usr
        user_name = usrnm
        firstname = fname
        


    def view_seatmatrix(self):
        print(self.seat_matrix)

    def find_record(self, name):
        # return 1 if record of name found, 0 otherwise.
        # if record found, print it here itself.
        with open('DataSheet.csv', 'r') as datasheet:
            csv_reader = reader(datasheet)
            for row in csv_reader:
                try:
                    if row[0]== name:
                        print("Applicant details: ")
                        for i in range(0,7):
                            print(row[i], end="   ")
                        return 1
                except IndexError:
                    return 0            
        return 0

    def append_to_csv(self, record):
        with open("DataSheet.csv", 'a+', newline="") as datasheet:
            csv_writer = writer(datasheet)
            csv_writer.writerow(record)

    def register(self):
        # search user name, if not found, create a new student record
        with open("signup_data.json", 'r') as signupdata:
            data= json.load(signupdata)
            if self.find_record(firstname)==0:
                print("Applicant details:\n")
                print("Name= " + data[user_name]["name"] +" "+data[user_name]["surname"])
                print("Email= "+data[user_name]["email"])
                marks= int(input("Enter your marks: "))
                print("\nPreference codes: (Computer:0, IT:1, Mechanical:2, Electronics:3)\n")
                pref1= int(input("Enter Preference 1:"))
                pref2= int(input("Enter Preference 2:"))
                pref3= int(input("Enter Preference 3:"))
                stud_rec=[data[user_name]["name"], data[user_name]["surname"], marks, data[user_name]["email"],pref1, pref2, pref3,"-"]
                self.append_to_csv(stud_rec)
                print("\nRegistration Successful!")
            else:
                print("\nYou have registered successfully.")
                

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
            print(f"This is the application status of {user_name}")
            pass
        if user==2:
            # for user= admin, show details of any student
            print("input the name of a student to search their details")
            pass

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
    
        if self.find_record(firstname):
            if mymachine.allotment_done== True:
                with open('DataSheet.csv', 'r') as datasheet:
                    csv_reader = reader(datasheet)
                    for row in csv_reader:
                        if row[0]== firstname:
                            print("Cannot Edit record now. Your allotment result is: "+ row[7])
                
            else:
                pass
                # with open('DataSheet.csv', 'r+') as datasheet:
                #     csv_writer = writer(datasheet)
                #     csv_reader= reader(datasheet)
                #     for row in csv_reader:
                #         if row[0]== firstname:
                #             print("\nName= "+ row[0] +" " + row[1])
                #             print("Marks= "+ row[2])
                #             row[3]= input("Enter your email id: ")
                #             row[4]=int(input("Enter preference 1: "))
                #             row[5]=int(input("Enter preference 2: "))
                #             row[6]=int(input("Enter preference 3: "))
                #             print("\nRecord updated successfully!")

        else:
            print("Student Record not found. Please register yourself.")           

    def delete_record(self):
        #allow only if allotment is not yet done
        if self.find_record(firstname):
            if mymachine.allotment_done== True:
                print("Cannot withdraw the application now. Allotment Process is done.")
            else:
                confirmation = (input("Do you wish to remove your record permanently? (press 'y'/'n') "))
                if confirmation == 'y' :
                    pass
                    # with open("DataSheet.csv",'a+') as datasheet:
                    #     csv_reader= reader(datasheet)
                    #     for row in csv_reader:
                    #         if row[0] != firstname:
                    #             writer.writerow(row) ; # write all non-matching rows
                    #         else:
                    #             pass
        
                    #     print("Your application was removed.")    
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


    