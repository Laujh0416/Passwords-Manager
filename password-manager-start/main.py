import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_numbers = random.randint(2, 4)
nr_symbols = random.randint(2, 4)

def generate_password():
    if len(password_input.get()) == 0:
        password_list = []
        password_list += [random.choice(letters) for i in range(nr_letters)]
        password_list += [random.choice(numbers) for i in range(nr_numbers)]
        password_list += [random.choice(symbols) for i in range(nr_symbols)]
        random.shuffle(password_list)
        password = "".join(password_list)
        password_input.insert(0, password)
        pyperclip.copy(password)
        messagebox.showinfo(title="Info",message="Password is copied!")
    else:
        password_input.delete(0, len(password_input.get()))
        generate_password()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    new_data = {website_input.get():{
        "Email":email_input.get(),
        "Password": password_input.get()
    }
    }
    if len(website_input.get()) == 0 or len(email_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please do not leave any field(s) empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, len(website_input.get()))
            password_input.delete(0, len(password_input.get()))


def retrieve_data():
    website_account = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
            messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website_account in data:
                email_data = data[website_account]["Email"]
                password_data = data[website_account]["Password"]
                messagebox.showinfo(title= website_account, message=f"Email: {email_data}\n Password: {password_data}")
        else:
            messagebox.showerror(message="No details for website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Passwords Manager")
icon =tkinter.PhotoImage(file = "logo3.png")
window.iconphoto(False, icon)
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
img = tkinter.PhotoImage(file = "logo2.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3)

label1 = tkinter.Label(text="Website:")
label1.grid(row=1, column=0)
label2 = tkinter.Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = tkinter.Label(text="Password:")
label3.grid(row=3, column=0)

website_input = tkinter.Entry(width=21)
website_input.grid(row=1, column=1, sticky="ew")
website_input.focus()
email_input = tkinter.Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_input.insert(0, "lau010416@gmail.com")
password_input = tkinter.Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")

button2 = tkinter.Button(text="Generate Password", command=generate_password, width=20)
button2.grid(row=3, column=2)
button1 = tkinter.Button(width=36, text="Add", command=save)
button1.grid(row=4, column=1, columnspan=2, sticky="ew")
search_button = tkinter.Button(text="Search", command=retrieve_data, width=20)
search_button.grid(row=1,column=2)

window.mainloop()