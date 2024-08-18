from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project from Day-5
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Sorry, website/password can not be empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                # Reading the old data
                data = json.load(data_file)
                # print(data) # loads python dictionary
                # updating old data with new data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)
            website_entry.focus()


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found")
    else:
        if website in data_dict:
            email = data_dict[website]["email"]
            password = data_dict[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There is no information for {website}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky=W)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky=W)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky=W)

# Input/Entry fields
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, pady=5)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.insert(END, "rakin@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, pady=5)

# Buttons
generate_password_button = Button(text="Generate Password", width=14,  command=generate_password)
generate_password_button.grid(row=3, column=2, pady=5)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text="Add")
add_button.config(width=43, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

window.mainloop()
