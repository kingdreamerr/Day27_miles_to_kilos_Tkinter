from tkinter import *

window = Tk()

def clear():
    value.config(text='0')
    input_tag.delete(0, END)


def convert():
    miles_value = float(input_tag.get())
    miles_to_kilometers = miles_value * 1.60934
    value.config(text=round(miles_to_kilometers))


input_tag = Entry(width=10)
input_tag.grid(column=1, row=0)

miles = Label(text="Miles",font=('Arial',15,'bold'))
miles.grid(column=2, row=0)

equal = Label(text='Is equal to',font=('Arial',15,'bold'))
equal.grid(column=0, row=1)

value = Label(text='0',font=('Arial',15,'bold'))
value.grid(column=1, row=1)

kilo = Label(text="Km",font=('Arial',15,'bold'),pady=10)
kilo.grid(column=2, row=1)

btn = Button(text='Calculate', command=convert, padx=5)
btn.grid(column=1, row=2)

clear_btn = Button(text='Clear', command=clear)
clear_btn.grid(column=2, row=2)
window.mainloop()