from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(0, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(0, 10))]
    password_numbers = [choice(numbers) for number in range(randint(0, 10))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def saved():
    web = website_entry.get()
    mail = email_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title='Huh, you left and empty field!', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"The are the details entered: \nEmail:{mail}\nPassword:"
                                                          f" {password}\n"f"Are you sure you want to save?")
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f'{web} | {mail} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP -----------------------------#
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
bg = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=bg)
canvas.grid(column=2, row=0)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'dano@mail.com')
password_entry = Entry(width=21)
password_entry.grid(column=2, row=3)

# Texts
web_entry = Label(text='Website:')
web_entry.grid(column=0, row=1)
mail_entry = Label(text='Email/Username:')
mail_entry.grid(column=0, row=2)
pass_entry = Label(text='Password:')
pass_entry.grid(column=0, row=3)

# Buttons
button1 = Button(text='Generate Password', command=password_generator)
button1.grid(column=4, row=3)
button1 = Button(text='Add', width=36, command=saved)
button1.grid(column=1, row=4, columnspan=2)

window.mainloop()