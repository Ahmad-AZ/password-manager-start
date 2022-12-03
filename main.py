import random
from tkinter import messagebox
from tkinter import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list+= [random.choice(symbols) for _ in range(nr_symbols)]
    password_list+= [random.choice(numbers) for _ in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    pwd_ent.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_ent.get()
    username=  user_ent.get()
    pwd = pwd_ent.get()

    if not (website and username and pwd):
        messagebox.showerror(title='Oops', message="Please don't leave any fields empty!")
    else:
        answer=messagebox.askyesno(title=website, message=f"These are the details entered: \nEmail: {username}\n"                                               f"Password: {pwd} \n ***is okay to save?***")
        if answer:
            with open('data.csv', mode = 'a') as file:
                file.write(f"{website}  |  {username}  |  {pwd} \n")
                pwd_ent.delete(0,END)
                website_ent.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Password Manager')
window.config(padx=30,pady=30)

canvas = Canvas(window,width= 200, height=200)
canvas.grid(row=0, column=1)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_img)



#labels
web_text= Label(window, text='Website:')
web_text.grid(row=1, column=0, pady=2)

user_text = Label(window, text= 'Email/Username:')
user_text.grid(row=2, column=0, pady=2)

pwd_text = Label(window, text='Password:')
pwd_text.grid(row=3, column=0, pady=2)


#entry
website_ent = Entry(window, width=50)
website_ent.focus()
website_ent.grid(row=1, column=1, columnspan=2,  pady=2)
website_input= website_ent.get()


user_ent= Entry(window, width=50)
user_ent.insert(END, 'ahmadabuzahra778@yahoo.com')
user_ent.grid(row=2, column=1, columnspan=2, pady=2)


pwd_ent= Entry(window, width=32)
pwd_ent.grid(row=3, column=1, pady=2)

#buttons
pwd_button= Button(window, text='Generate Password', command=gen_pwd)
pwd_button.grid(row=3, column=2, pady=2)

add_button = Button(window, text ='Add', width= 43, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=2)



window.mainloop()

