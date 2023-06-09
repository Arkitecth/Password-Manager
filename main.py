from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    char_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = char_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
                # Update the old daya with new daya
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #


def search():
    website_name = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
            if website_name in data:
                messagebox.showinfo(title="Hello",
                                    message=f"Email:{data[website_name]['email']}\n Password:{data[website_name]['password']}\n")
            else:
                messagebox.showinfo(
                    title="Oops", message="No Data Found")
    except FileNotFoundError:
        messagebox.showinfo(
            title="Oops", message="You have not created a file")


        # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
password_img = canvas.create_image(150, 100, image=img)
canvas.grid(row=0, column=1)


# Website
webiste_label = Label(text="Website:")
webiste_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)


# Email
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "QF@gmail.com")


# Password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate Password Button
generate_password_btn = Button(
    text="Generate Password", command=generate_password)
generate_password_btn.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

# Search Button
search_button = Button(text="Search", command=search)
search_button.grid(column=3, row=1)


window.mainloop()
