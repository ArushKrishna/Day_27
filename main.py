from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500,300)

label = Label(text='I am a label', font=('Arial', 24, "bold"))
label.pack()

label['text'] = 'New Text'
label.config(text='New Text')

#Button

def button_clicked():
    label.config(text=input.get())


button = Button(text='Click Me', command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())




window.mainloop()