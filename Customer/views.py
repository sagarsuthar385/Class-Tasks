
all_laptop={

"dell":65000,
"hp":20000,
"lenovo":655555,


}
all_mobile={
"samsung":326565,
"apple":2000000,
"vivo":3000

}
customber_cart={}

def viewlaptop():
    print("\n laptop list:\n")
    for k,v in all_laptop.items():
        print(f"{k}={v}")
def viewmobile():
    for k,v in all_mobile.items():
        print(f"{k}={v}")
def purchaselaptop(laptop_name,qty):
    if laptop_name in all_laptop:
        price=all_laptop[laptop_name]
        total_price=qty*price
        print("total_price=",total_price)
def purchasemobile(mobile_name,qty):
    if mobile_name in all_mobile:
        price=all_mobile[mobile_name]
        total_price=qty*price
        print("total_price=",total_price)
def addtocart(custombername, product,productname,qty,total_price):
    specification={}
    if custombername not in customber_cart:
        specification["product_name"]=productname
        specification["qty"]=qty
        specification["total_price"]=total_price
        customber_cart[custombername]=specification
        print(customber_cart)


    

