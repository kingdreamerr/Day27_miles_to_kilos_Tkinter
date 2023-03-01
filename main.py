from tkinter import *

window = Tk()

input_tag = Entry(width=10)
input_tag.grid(column=1, row=0)

miles = Label(text="Miles",font=('Arial',15,'bold'))
miles.grid(column=2, row=0)

window.mainloop()