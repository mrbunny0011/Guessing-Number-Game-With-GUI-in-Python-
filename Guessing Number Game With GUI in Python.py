#      Guessing Number Game

from tkinter import *
from tkinter import messagebox
import random

jackpot=random.randint(1,10)
chance=0
msg=""

# Function for chack the number
def get_number():
    global chance,msg
    num=int(number.get())
    
    if num<jackpot:
        chance+=1
        msg=f'{chance} attampt.'
        messagebox.showinfo("Result","Guess Higher Number")
        
    elif num>jackpot:   
        chance+=1
        msg=f'{chance} attampt.'
        messagebox.showinfo("Result","Guess Lower Number")
        
    elif num==jackpot:
        
        chance+=1
        msg=f'You use {chance} attampts.'
        messagebox.showinfo("Result","Great you win ")
    disp.set(msg)
        

root=Tk()
disp=StringVar()
root.title("Guessing Number Game")
root.geometry("350x350")
root.resizable(0,0)
root.configure(bg="#FFA500")

# Hading TEXT
name=Label(text="Guess your number in (1 to 10)",bg="#FFA500",fg="black")
name.pack(pady=(20,10))
name.config(font=("vardana",15,'bold'))

# Entry 
number=Entry(root,width=10)
number.pack(ipady=8,pady=(0,15))
number.config(font=("vardana",15,'bold'))

# Chack Button
btn=Button(root,text="Check",bg="#AA6C39",fg="white",width=5,height=2,command=lambda:get_number())
btn.pack(pady=(20,10))
btn.config(font=("vardana",14))

# Message TEXT
Label(root,
    textvariable=disp,
    font=("vardan",15),
    bg="#FFA500",fg="black"
).pack(pady=(20,10))




root.mainloop()