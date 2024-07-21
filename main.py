from tkinter import *
from tkinter import messagebox
from Pass_Generator import Password_generator
import pyperclip3
import json

# Generate Function
Pass_Gen = Password_generator()


def generate_password():
    if len(password_entry.get()) > 0:
        messagebox.showerror("Ooops", "Password already generated")
    else:
        password = Pass_Gen.create_password()
        password_entry.insert(0, password)
        pyperclip3.copy(password)
# Add function


def add():

    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if not (email and website and password):
        messagebox.showerror("Ooops", "Some fields are empty")
    else:
        try:
            with open("Password manager.json", "r") as file:
               data = json.load(file)
        except FileNotFoundError:
            with open("Password manager.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("Password manager.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# search function
def search():
    website = website_entry.get().title()
    if not website:
        messagebox.showerror("Ooops", "Enter some text to search")
    else:
        try:
            with open("Password manager.json", "r") as file:
                data = json.load(file)
                if website in data:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    messagebox.showinfo(website, f"email :{email}\npassword :{password}")
                else:
                    raise KeyError
        except KeyError:
            messagebox.showerror("Ooops", f"There is no data for {website}")
        except FileNotFoundError:
            messagebox.showerror("Ooops", "There is no file")


# Create the main window

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=50)

# Canvas for the logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=41)
email_entry.grid(row=2, column=1, columnspan=3)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

# Start the main loop
window.mainloop()
