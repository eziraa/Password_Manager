import json
import random
from tkinter import *
from tkinter import messagebox

window = Tk()
window.minsize(500, 500)
window.title("Password Manager")
window.config(padx=20, pady=20)
window.config(bg="white")


def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't''u', 'v', 'w', 'x', 'y', 'z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S',
               'T''U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    number = [random.choice(numbers) for _ in range(random.randint(8, 10))]
    symbol = [random.choice(symbols) for _ in range(random.randint(4, 6))]
    letter = [random.choice(letters) for _ in range(random.randint(4, 6))]
    generated_password = number + letter + symbol
    random.shuffle(generated_password)
    password = "".join(generated_password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


def is_valid_inputs(website, email, password):
    if website == "":
        messagebox.showerror(title="Warning", message="The website field is empty")
        return False
    elif email == "":
        messagebox.showerror(title="Warning", message="The email field is empty")
        return False
    elif password == "":
        messagebox.showerror(title="Warning", message="The password field is empty")
        return False
    else:
        return True


def save():
    website = web_name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    to_be_written = {website: {
        "email": email,
        "password": password
    }}
    if is_valid_inputs(website=website, email=email, password=password):
        try:
            with open("data.json", "r") as file_read:
                # Loading data
                data = json.load(file_read)
                # Updating data
                data.update(to_be_written)
        except FileNotFoundError:
            with open("data.json", "w") as file_write:
                json.dump(to_be_written, file_write, indent=4)
                web_name_entry.delete(0, END)
                password_entry.delete(0, END)
                web_name_entry.focus()
                messagebox.showinfo("Show successes", message="The information in saved successfully")
        else:
            with open("data.json", "w") as file_write:
                json.dump(data, file_write, indent=4)
                web_name_entry.delete(0, END)
                password_entry.delete(0, END)
                web_name_entry.focus()
                messagebox.showinfo("Show successes", message="The information in saved successfully")


image = PhotoImage(file="logo.png")
canvas = Canvas(bg="white", width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1, columnspan=2)

# Labels
web_name_label = Label(text="Website", bg="white")
web_name_label.grid(row=1, column=0)
email_label = Label(text="Email/Username   ", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password", bg="white")
password_label.grid(row=3, column=0)

# Entries
web_name_entry = Entry(width=50)
web_name_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ezra@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)
# Buttons
generate_btn = Button(text="Generate Password", width=16, command=generatePassword)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", width=42, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
