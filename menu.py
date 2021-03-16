from os import system, name
from database import *
import time

mydata= Data() #object of class Data

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')


class Menu:
  def __init__(self):
    
    self.user= None

    self.student_menu = """
                                                         MENU
                                            ----------------------------------
                                            |  1. View Seat Matrix.          |
                                            |  2. Register.                  |
                                            |  3. Check application status   |
                                            |  4. Edit your application      |
                                            |  5. Withdraw application       |
                                            |  6. View cutoff marks          |
                                            |                                |
                                            |  7. Logout.                    |
                                            ----------------------------------
      """
    self.admin_menu= """
                                                        MENU
                                --------------------------------------------------------            
                                |  1. Run Seat Allotment Process.                      |
                                |  2. View all student registrations.                  |
                                |  3. View full allotment result.                      |
                                |  4. View branchwise allotment list.                  |
                                |  5. Search a student.                                |
                                |  6. View list of students left without allotment.    |
                                |  7. Get data of vacancies left.                      |
                                |                                                      |
                                |  8. Log out.                                         |
                                --------------------------------------------------------
      """
    self.login_menu= """
                                                      MENU
                                            ---------------------------------
                                            |  1. Sign up(only for student) |
                                            |  2. Login as Student          |
                                            |  3. Login as Admin            |
                                            |  4. Exit portal               |
                                            --------------------------------
      """

  def login(self):
    clear()  
    print(self.login_menu)
    user_inp = int(input("Enter your choice: "))
    
    while (user_inp > 4 or user_inp < 1):
        user_inp = int(input("Invalid. Enter your choice again: "))

    # store who is the current user in class var- user.   
    self.user = user_inp
    
    if user_inp==1:
        # signup for students is selected
        clear()
        mydata.student_sign_up()
    
    if user_inp==2 :
        # login as student is selected
        name = input("Enter user name: ")
        mydata.set_userinfo(2,name) # send user info to database file
        is_correct_pswd = mydata.check_pswd(name)
        if(is_correct_pswd==1):  # name and password match
            print(f"\n Welcome, {name.capitalize()}!")
            time.sleep(2)
            return
        else:
            # Username or password or both do not match
            print("Sorry! Incorrect credentials. ") 
            self.login()
        
    if user_inp ==3:
        # login as admin is selected
        # (pwd for admin is 12345)
        pwd= input("Enter password:")
        if (pwd =="12345"):
            print("Welcome, Admin!")
            mydata.set_userinfo(3,"admin") # send user info to database file
            time.sleep(2)
        else:
            print("Sorry wrong password! ")
            self.login()


  def menu_for_student(self):
    clear() 
    choice= None 
    while(choice!=7): # breaks out of loop when 7 i.e. logout is selected
        if mydata.flag==0: 
            # flag=0 indicates user has not withdrawn his application.
            print(self.student_menu)
            choice= int(input("Enter your choice: "))
        else: 
            # flag=1 is the case where user has withdrawn the application. So we do not show him any other option and force him to logout.
            choice=7
        while(choice>7 or choice <1):
            choice = int(input("Invalid. Enter your choice again: "))
        if choice!=7:
            # when any choice other than logout is selected, call the corresponding function from the functions list in database.py
            clear()
            mydata.student_options[choice-1](mydata) 
    return


  def menu_for_admin(self):
    clear() 
    choice= None 
    while(choice!=8):  # breaks out of loop when 8 i.e. logout is selected
        print(self.admin_menu)
        choice= int(input("Enter your choice: "))
        while(choice>8 or choice <1):
            choice = int(input("Invalid. Enter your choice again: "))

        if choice!=8:
            # when any choice other than logout is selected, call the corresponding function from the functions list in database.py
            clear()
            if choice!=1:
                # all functions other than 'run allotment' are present in class Data. They require an object of this class to be passed as parameter.
                mydata.admin_options[choice-1](mydata)   
            else:
                # if choice 1 is selected, this run allotment function is present in a diff class than other functions and hence does not require the object of class Data to be passed as paramenter.
                mydata.admin_options[0]()      
    return
