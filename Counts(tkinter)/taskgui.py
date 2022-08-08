
from ast import Expression, Global
from pickle import GLOBAL, TRUE
import tkinter

screen=tkinter.Tk()
screen.geometry=("500x500")
screen.configure(bg="gray")
c=0
def button():
   while True: 
    global c
    c=c+1
    print("Total likes= ",c)
    print("      ")
    break
def button2():
    while True:
        global c
        c=c+1
        print("Total dis-likes= ",c)
        print("    ")
        break
        
        
    
      
   
lbl=tkinter.Label(screen,text="Do you like python language\n or not ?",font=("arial",10,"bold"),bg="gray")
lbl.place(x=10,y=10)

btn=tkinter.Button(screen,text="like",font=("arial",6,"bold"),command=lambda :button())
btn.place(x=50,y=60)



btn=tkinter.Button(screen,text="dis-like",font=("arial",6,"bold"),command=lambda :button2())
btn.place(x=110,y=60)


lbl=tkinter.Label(screen,text="Thank you !!",font=("arial",8,"bold"),bg="gray")
lbl.place(x=60,y=90)




screen.mainloop()
