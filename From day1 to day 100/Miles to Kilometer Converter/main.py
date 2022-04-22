from tkinter import *

def miles_to_kms():
    miles_input = float(miles.get())
    kms = miles_input * 1.609
    kilometer_result.config(text=f"{kms}")

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=15, pady=15)

#The information input box
miles = Entry(width=10)
miles.grid(column=1, row=0)


miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

kilometer_result = Label(text='0')
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text='Km')
kilometer_label.grid(column=2, row=1)

#The button used to convert the currencys
button = Button(text='Calculate', command=miles_to_kms)
button.grid(column=1, row=2)

window.mainloop()
