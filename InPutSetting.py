

from tkinter.constants import ACTIVE
from typing import DefaultDict

import tkinter as tk

window =tk.Tk()
window.geometry("300x200")
window.title("SQL Configuration")

User_var = tk.StringVar()
PassWord_var = tk.StringVar()
Host_var = tk.StringVar()
DataBase_var = tk.StringVar()
tb_var = tk.StringVar()

#!-----default sql configuration--------

User = "root"
PassWord = "root"
Host = "127.0.0.1"
DataBase = ""
tb = ""
#!-------------------------------------



def submit(event=None):
    global User, PassWord, Host, DataBase, tb
    User = User_var.get()
    PassWord = PassWord_var.get()
    Host = Host_var.get()
    DataBase = DataBase_var.get()
    tb = tb_var.get()
    window.destroy()



label_user = tk.Label(text="Username: ",  font=("console", 11))
entry_user =tk.Entry(font=("console", 10), textvariable=User_var)
entry_user.insert(0,User)

label_pass = tk.Label(text="Password: ",   font=("console", 11))
entry_pass =tk.Entry(font=("console", 10), textvariable=PassWord_var)
entry_pass.insert(0,PassWord)

label_host = tk.Label(text="Hostname: ",  font=("console", 11))
entry_host =tk.Entry(font=("console", 10),textvariable=Host_var)
entry_host.insert(0,Host)

label_database = tk.Label(text="Database: ",  font=("console", 11))
entry_database =tk.Entry(font=("console", 10), textvariable=DataBase_var)

label_table = tk.Label(text="Tablename: ",  font=("console", 11))
entry_table =tk.Entry(font=("console", 10), textvariable=tb_var)

btn =tk.Button(
    window, 
    text="Submit", 
    command= submit, 
    background="white",
    activebackground="green",
    width=8,
    height=2,
    default="active",
    underline=0,
    font=("Segoe UI Black", 10)
)



label_user.grid(row=0, column=0)
entry_user.grid(row=0, column=1)
label_pass.grid(row=1, column=0)
entry_pass.grid(row=1, column=1)
label_host.grid(row=2, column=0)
entry_host.grid(row=2, column=1)
label_database.grid(row=3, column=0)
entry_database.grid(row=3, column=1)
label_table.grid(row=4, column=0)
entry_table.grid(row=4, column=1)
btn.grid(row=5, column=1)


window.bind("<Return>", submit)



window.mainloop()



if (DataBase=="" or tb==""):
    print("\n please enter Database or tabel name!\n")
    exit()