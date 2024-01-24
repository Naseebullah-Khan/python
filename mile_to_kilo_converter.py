from tkinter import Tk, Label, Button, Entry, END


def converter():
    convert = round(float(mile.get()) * 1.609)
    label3.config(text=f"{convert}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile = Entry(width=7)
mile.grid(column=2, row=0)

label1 = Label(text="Miles")
label1.grid(column=3, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="0")
label3.grid(column=2, row=1)

label4 = Label(text="Km")
label4.grid(column=3, row=1)

converter_btn = Button(text="Converter", command=converter)
converter_btn.grid(column=2, row=3)

window.mainloop()
