
from menu import Menu

mymenu= Menu()  # obj of class Menu

while(mymenu.user!=4):  # end program when option 4 i.e. exit portal is selected.
    mymenu.login()
    if mymenu.user==2:
        mymenu.menu_for_student()
    elif mymenu.user==3:
        mymenu.menu_for_admin()
    
print("Goodbye.")        
