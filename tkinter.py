from tkinter import *

window = Tk()

# keeps the window on the screen for users to interact with it

# title of program
window.title("my first GUI program")
# adjust the gui screen size
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="papjm from Hackerone", font=("Arial", 24, "bold"))
my_label.pack()



button = Button(text="Click me")







window.mainloop()