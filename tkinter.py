from tkinter import *

window = Tk()

# keeps the window on the screen for users to interact with it

# title of program
window.title("my first GUI program")
# adjust the gui screen size
window.minsize(width=500, height=300)

my_label = Label(text="papjm from Hackerone", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    print("i got clicked")
    my_label.config(text="Button got clicked")

button = Button(text="Click me", command=button_clicked)
button.pack()


#DATA Entry

input = Entry(width=10)
input.pack()
input.get()



window.mainloop()
