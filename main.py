from tkinter import *
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Generate a random password with a combination of letters, digits, and symbols
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = emai_entry.get()
    password = pass_entry.get()

    if website and email and password:
        with open("passwords.txt", "a") as file:
            file.write(f"Website: {website} | Email/Username: {email} | Password: {password}\n")
        web_entry.delete(0, END)
        emai_entry.delete(0, END)
        pass_entry.delete(0, END)
        save_label.config(text="Password saved successfully", fg="green", font=10)
        window.after(10000, lambda: save_label.config(text=""))

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
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
emai_entry = Entry(width=35)
emai_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=24)
pass_entry.grid(row=3, column=1)

# Buttons
btn_gen = Button(window, text="Generate", command=generate_password)
btn_gen.grid(row=3, column=2)
btn_add = Button(text="Add", width=33, command=save_password)
btn_add.grid(row=4, column=1, columnspan=2)

# Save Label
save_label = Label(text="", width=36, pady=5)
save_label.grid(row=5, column=1, columnspan=2)

window.mainloop()

