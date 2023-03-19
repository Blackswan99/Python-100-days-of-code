from tkinter import *
WHITE = "#ffffff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=WHITE)

photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=WHITE)
canvas.create_image(100,100,image=photo)
canvas.grid(column=2, row=0)

website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username:", bg=WHITE)
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate password", highlightthickness=0, )
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", width=36, highlightthickness=0)
add_button.grid(column=2, row=4, columnspan=2)

window.mainloop()
