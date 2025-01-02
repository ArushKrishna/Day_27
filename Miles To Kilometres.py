from tkinter import *

def calculate():
    miles = float(miles_input.get())
    miles *= 1.609
    result_label.config(text=str(miles))

window = Tk()
window.title('Miles to Kilometer Converter')
window.config(padx=50,pady=50)

miles_input = Entry(width= 10)
miles_input.grid(column=1 ,row=0 )

miles_label = Label(text='Miles')
miles_label.grid(column=2 ,row=0 )

result_label = Label(text='0')
result_label.grid(column=1 ,row=1 )

km_label = Label(text = 'Km')
km_label.grid(column=2 ,row=1 )

equals = Label(text='is equal to')
equals.grid(column=0 ,row=1 )

calculate_button = Button(text='Calculate', command=calculate)
calculate_button.grid(column=1 ,row=2 )

window.mainloop()
