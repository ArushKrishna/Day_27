from tkinter import *
window = Tk()

label = Label(text='Hi')
button = Button(text='Click Me')
new_button = Button(text="Don't Click Me")
entry = Entry(width=10)

label.grid(row=0,column=0)
new_button.grid(row=0,column=2)
button.grid(row=1,column=1)
entry.grid(row=2,column=3)

window.mainloop()