
from menu import Menu

mymenu= Menu()

while(mymenu.user!=3):
    mymenu.login()1
    if mymenu.user==1:
        mymenu.menu_for_student()
    elif mymenu.user==2:
        mymenu.menu_for_admin()
    
print("Goodbye.")        
