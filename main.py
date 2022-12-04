import json
import random
from tkinter import messagebox
from tkinter import *
import pyperclip




# ---------------------------- Search a Website ------------------------------- #

def search_web():
    website = website_ent.get()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found.')
    else:
        if website in data:
            email= data[website]['email']
            pwd = data[website]['pwd']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {pwd}")
        else:
            messagebox.showinfo(title='Not Found', message=f"No details for the {website} exists.")










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

def write_data(file_path, mode='r'):

    file =  open(file_path, mode)
    return file

def save():

    website = website_ent.get().title()
    username=  user_ent.get()
    pwd = pwd_ent.get()
    new_data = {
        website:{
            "email": username,
            "pwd":pwd
        }
    }
    if not (website  and pwd):
        messagebox.showerror(title='Oops', message="Please don't leave any fields empty!")
    else:
        try:
            file = write_data('data.json', mode='r')
            data_s = json.load(file)
            # with open('data.json', mode='r') as file:
            #      data = json.load(file)


        except FileNotFoundError :
            new_file = write_data('data.json', mode='w')
            json.dump(new_data, new_file, indent=4)
            # with open('data.json', mode='w') as new_file:
            #     # write data to the file
            #     json.dump(new_data, new_file , indent=4)
        else:
            f = write_data('data.json', mode='w')
            data_s.update(new_data)
            json.dump(data_s, f, indent=4)
            # appending to old data
            #data.update(new_data)
            # with open('data.json', mode='w') as file:
            #          json.dump(data, file, indent=4)
        finally:
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
website_ent = Entry(window, width=32)
website_ent.focus()
website_ent.grid(row=1, column=1, pady=2)
website_input= website_ent.get()


user_ent= Entry(window, width=50)
user_ent.insert(END, 'ahmadabuzahra778@yahoo.com')
user_ent.grid(row=2, column=1, columnspan=2, pady=2)


pwd_ent= Entry(window, width=32)
pwd_ent.grid(row=3, column=1, pady=2)

#buttons
pwd_button= Button(window, text='Generate Password', command=gen_pwd)
pwd_button.grid(row=3, column=2, pady=2)

search_button= Button(window, text='Search', width= 14,  command=search_web)
search_button.grid(row=1, column=2, pady=2)

add_button = Button(window, text ='Add', width= 43, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=2)



window.mainloop()

