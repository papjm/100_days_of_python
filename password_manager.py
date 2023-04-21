from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.pack()


#Labels
website_label = Label(text="Website")
email_label = Label(text="Email/Username")
password_label = Label(text="password")


window.mainloop()