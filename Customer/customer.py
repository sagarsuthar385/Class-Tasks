
from views import *
name= input("Enter your name= ")
Menu="""
      menu
      1) laptop
      2) mobile
"""
print(Menu)
choice=int(input("Enter your choice= "))
if choice==1:
    viewlaptop()
    laptop_name=input("Enter laptop name you want to buy= ")
    qty=int(input("Enter no of quantity= "))
    total_price = purchaselaptop(laptop_name,qty)
    choice=input("Do you want to purchase it press y for yes= ")
    if choice=='y'or 'yes':
        addtocart(name,"laptop",laptop_name,qty,total_price)
        purchaselaptop(laptop_name,qty)
elif choice==2:
    viewmobile()
    mobile_name=input("Enter mobile name you want to buy= ")
    qty=int(input("Enter no of quantity= "))
    total_price = purchasemobile(mobile_name,qty)
    choice=input("do you want to purchase it press y for yes ")
    if choice=='y'or 'yes':
        addtocart(name,"MOBILE",mobile_name,qty,total_price)
        purchasemobile(mobile_name,qty)
    
else:
    print("invalid")