from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import choice, randint , shuffle
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(letters) for _ in range(randint(2, 4))]
    password_numbers=[choice(letters) for _ in range(randint(2, 4))]
    password_list=password_letters+password_symbols+password_numbers

    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website) ==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="Please make sure haven't left any fields")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered:\n Email:{email} \n Password:{password}\n Is it ok to save?")
    file_path=r"C:\Users\USER\Documents\Python_Projects\Password_manager"
    
    if is_ok:
        with open("file_path", "a") as data1_file:
            data1_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,END)      #delete the previous data entered
            password_entry.delete(0,END)
        
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file=r"C:\Users\USER\Documents\Python_Projects\Password_manager\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=1)
email_entry.insert(0,"sushant@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)


generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=1)

window.mainloop()
