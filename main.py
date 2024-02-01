from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = emai_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", icon="info", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data in new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updating data
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- FINED PASSWORD ------------------------------- #
def fined_password():
    website = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
        print("No data file found")
    else:
        if website.lower() in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exist.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=24)
web_entry.grid(row=1, column=1)
emai_entry = Entry(width=35)
emai_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=24)
pass_entry.grid(row=3, column=1)

# Buttons
btn_gen = Button(window, text="Generate", padx=5, command=generate_password)
btn_gen.grid(row=3, column=2)
btn_add = Button(text="Add", width=33, command=save_password)
btn_add.grid(row=4, column=1, columnspan=2)
btn_search = Button(text="Search", padx=10, command=fined_password)
btn_search.grid(row=1, column=2)

# Save Label
save_label = Label(text="", width=36, pady=5)
save_label.grid(row=5, column=1, columnspan=2)

window.mainloop()
