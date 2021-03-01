from os import system, name
from database import *
import time

mydata= Data()

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')


class Menu:
  def __init__(self):
    
    self.user= None
    self.username= None

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
                                            --------------------------        
                                            |  1. Login as Student   |
                                            |  2. Login as Admin     |
                                            |  3. Exit portal        |
                                            --------------------------
      """

  def login(self):
    clear()  
    print(self.login_menu)
    user_inp = int(input("Enter your choice: "))
    
    while (user_inp > 3 or user_inp < 1):
        user_inp = int(input("Invalid. Enter your choice again: "))
    self.user = user_inp
    if self.user!=3:
        self.username = input("Enter user name: ")
        mydata.set_userinfo(self.user, self.username)
        print(f"\n Welcome, {self.username.capitalize()}!")
        time.sleep(2)
        
  def menu_for_student(self):
    clear() 
    choice= None 
    while(choice!=7):
        print(self.student_menu)
        choice= int(input("Enter your choice: "))
        while(choice>7 or choice <1):
            choice = int(input("Invalid. Enter your choice again: "))

        
        if choice!=7:
            clear()
            mydata.student_options[choice-1](mydata)    
      
    return
    # self.login()

  def menu_for_admin(self):
    clear() 
    choice= None 
    while(choice!=8):
        print(self.admin_menu)
        choice= int(input("Enter your choice: "))
        while(choice>8 or choice <1):
            choice = int(input("Invalid. Enter your choice again: "))

        if choice!=8:
            clear()
            if choice!=1:
                mydata.admin_options[choice-1](mydata)   
            else:
                mydata.admin_options[0]()    
        
    return
    # self.login() 