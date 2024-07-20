from tkinter import *
from tkinter import messagebox
from Pass_Generator import Password_generator
import pyperclip3

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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if not (email and website and password):
        messagebox.showerror("Ooops", "Some fields are empty")
    else:
        is_0k = messagebox.askokcancel(title=website, message=f"The details are\nEmail:{email}\nPassword:{password}"
                                       f"\nDo you want to save these details?")
        if is_0k:
            with open("Password manager.txt", "a") as file:
                file.write(f"Website :{website} \nEmail :{email}, Password :{password}\n\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)

# Start the main loop
window.mainloop()
