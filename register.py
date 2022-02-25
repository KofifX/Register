#discord : pakpak#5600

import tkinter as tk
from tkinter import *

root=tk.Tk()
 
root.geometry("600x400")
  

name_var=tk.StringVar()
passw_var=tk.StringVar()
ema_var=tk.StringVar()
 
  
def submit():
 
    name=name_var.get()
    password=passw_var.get()
    email=ema_var.get()

    print("information the user entered")
    print("⬇⬇⬇") 
    print("The username is : " + name)
    print("The password is : " + password)
    print("the Email is : " + email)
     
    name_var.set("")
    passw_var.set("")
    ema_var.set("")
     
     

name_label = tk.Label(root, text = 'Username', font=('calibre',20, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',20,'normal'))
  

passw_label = tk.Label(root, text = 'Password', font = ('calibre',20,'bold')) 
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',20,'normal'), show = '*')

email_label = tk.Label(root, text = 'Email', font=('calibre',20, 'bold'))
email_entry = tk.Entry(root,textvariable = ema_var, font=('calibre',20,'normal'))

sub_btn = tk.Button(text='Send',command=submit, bg='brown',fg='white', font = ('calibre',16,'bold'))

name_label.grid(row=0,column=50)
name_entry.grid(row=0,column=51)
passw_label.grid(row=1,column=50)
passw_entry.grid(row=1,column=51)
email_label.grid(row=2,column=50)
email_entry.grid(row=2,column=51)
sub_btn.grid(row=3,column=51)


root.mainloop()
