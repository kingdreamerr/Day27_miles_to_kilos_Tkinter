from tkinter import *

window = Tk()

input_tag = Entry(width=10)
input_tag.grid(column=1, row=0)

miles = Label(text="Miles",font=('Arial',15,'bold'))
miles.grid(column=2, row=0)

equal = Label(text='Is equal to',font=('Arial',15,'bold'))
equal.grid(column=0, row=1)

value = Label(text='0',font=('Arial',15,'bold'))
value.grid(column=1, row=1)
window.mainloop()