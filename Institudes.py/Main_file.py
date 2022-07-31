import Faculty,Student
print("          ")
print("--------------------------------------------------------------")
print("----------------------Institute Detail------------------------")
print("          ")
status=True
while status:
    choice=input("Do you want to make detail press'f' for faculty and press 's' for student= ") 
    if choice=="f":
        name=input("Enter your name= ")
        position=input("Enter your postion in this institute= ")
        subject=input("Enter your teaching subject= ")
        contact_no=int(input("Enter your contact number= "))
        email=input("Enter your email address= ")
        score=int(input("Enter the score= "))
        city=input("Enter your city name= ")
        print("            ")
        print("------------------------------------------------------")   
        f=Faculty.facultyclass() 
        f.create_faculty(name,position,subject,contact_no,email,score,city)
        print("------------------------------------------------------")   
        print("            ")

    else:
        name=input("Enter your name= ")
        Institude_name=input("Enter your institute name= ")
        Class=int(input("Enter your class= "))
        contact_no=int(input("Enter your contact number= "))
        email=input("Enter your email address= ")
        score=int(input("Enter the score= "))
        city=input("Enter your city name= ")
        print("            ")
        print("------------------------------------------------------")    
        f=Student.studentclass() 
        f.create_student(name,Institude_name,Class,contact_no,email,score,city)  
        print("------------------------------------------------------")   
        print("            ")

    choice=input("Do you want to make detail press'y' for yes and press 'n' for no= ")
    if choice=='y':
        status=True
    else:
        status=False
            

           
